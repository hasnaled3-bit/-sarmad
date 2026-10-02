# -*- coding: utf-8 -*-
"""
مستودع الذاكرة (Memory Store)
نظام الحفظ والاسترجاع الدائم.
هذا ما يجعل النواة "تتعلم" من التاريخ.
"""

from typing import Dict, List, Optional, Any
from datetime import datetime
import json
import os
from pathlib import Path


class MemoryStore:
    """
    مستودع الذاكرة: نظام حفظ واسترجاع الذاكرة الدائم.
    
    الذاكرة تتكون من:
    - السياق: الخلفية والظروف
    - الأحداث: ما حدث
    - المعاني: ما تعلمناه
    - الروابط: كيف يرتبط كل شيء
    """

    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        
        self.memory_file = self.data_dir / "memory.json"
        self.decisions_file = self.data_dir / "decisions.json"
        self.learning_file = self.data_dir / "learning.json"
        
        self.memory = self._load_memory()
        self.creation_time = datetime.now()

    def _load_memory(self) -> Dict:
        """
        تحميل الذاكرة من الملف.
        """
        if self.memory_file.exists():
            try:
                with open(self.memory_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"خطأ في تحميل الذاكرة: {e}")
        
        return self._create_empty_memory()

    def _create_empty_memory(self) -> Dict:
        """
        إنشاء ذاكرة فارغة.
        """
        return {
            "contexts": [],
            "events": [],
            "meanings": [],
            "relationships": [],
            "learned_patterns": {},
            "decisions": [],
            "created_at": datetime.now().isoformat()
        }

    def save_to_disk(self) -> bool:
        """
        حفظ الذاكرة على القرص الصلب.
        """
        try:
            with open(self.memory_file, 'w', encoding='utf-8') as f:
                json.dump(self.memory, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"خطأ في حفظ الذاكرة: {e}")
            return False

    def add_context(self, context_text: str, tags: Optional[List[str]] = None) -> Dict:
        """
        إضافة سياق جديد.
        """
        context = {
            "id": len(self.memory["contexts"]),
            "text": context_text,
            "tags": tags or [],
            "timestamp": datetime.now().isoformat(),
            "importance": self._calculate_importance(context_text)
        }
        
        self.memory["contexts"].append(context)
        self.save_to_disk()
        return context

    def add_event(self, event_text: str, action: Optional[str] = None, decision: Optional[Dict] = None) -> Dict:
        """
        إضافة حدث جديد.
        """
        event = {
            "id": len(self.memory["events"]),
            "text": event_text,
            "action": action,
            "decision": decision,
            "timestamp": datetime.now().isoformat(),
            "learned": False
        }
        
        self.memory["events"].append(event)
        self._extract_learning_from_event(event)
        self.save_to_disk()
        return event

    def add_meaning(self, meaning_text: str, source: Optional[str] = None, related_to: Optional[List[str]] = None) -> Dict:
        """
        إضافة معنى (درس مستفاد).
        """
        meaning = {
            "id": len(self.memory["meanings"]),
            "text": meaning_text,
            "source": source or "self-reflection",
            "related_to": related_to or [],
            "timestamp": datetime.now().isoformat(),
            "strength": 1  # كم مرة تكررنا هذا الدرس
        }
        
        self.memory["meanings"].append(meaning)
        self.save_to_disk()
        return meaning

    def create_relationship(self, entity1: str, relation: str, entity2: str, strength: int = 1) -> Dict:
        """
        إنشاء علاقة بين شيئين.
        """
        relationship = {
            "entity1": entity1,
            "relation": relation,
            "entity2": entity2,
            "strength": strength,
            "timestamp": datetime.now().isoformat()
        }
        
        # البحث عن علاقة موجودة وتقويتها
        for existing in self.memory["relationships"]:
            if (existing["entity1"] == entity1 and 
                existing["relation"] == relation and 
                existing["entity2"] == entity2):
                existing["strength"] += 1
                self.save_to_disk()
                return existing
        
        self.memory["relationships"].append(relationship)
        self.save_to_disk()
        return relationship

    def _extract_learning_from_event(self, event: Dict) -> None:
        """
        استخراج الدروس المستفادة من الحدث.
        """
        if not event.get("decision"):
            return
        
        decision = event["decision"]
        key = decision.get("status", "neutral")
        
        if key not in self.memory["learned_patterns"]:
            self.memory["learned_patterns"][key] = {
                "count": 0,
                "examples": [],
                "average_score": 0
            }
        
        pattern = self.memory["learned_patterns"][key]
        pattern["count"] += 1
        pattern["examples"].append(decision.get("action", ""))
        
        # حساب المتوسط
        all_scores = [d.get("score", 0) for d in self.memory["learned_patterns"][key]["examples"]]
        if all_scores:
            pattern["average_score"] = sum(all_scores) / len(all_scores)

    def _calculate_importance(self, text: str) -> int:
        """
        حساب أهمية النص (من 1 إلى 10).
        """
        # كلمات مهمة جداً
        critical_words = ["عهد", "خيانة", "موت", "حياة", "حق", "ظلم"]
        # كلمات مهمة
        important_words = ["حب", "رحمة", "نية", "اختيار", "قرار"]
        
        importance = 5  # القاعدة
        
        for word in critical_words:
            if word in text:
                importance = 10
                break
        
        for word in important_words:
            if word in text:
                importance = max(importance, 8)
        
        return importance

    def recall(self, query: str, limit: int = 5) -> Dict:
        """
        استرجاع الذاكرة بناءً على استعلام.
        """
        results = {
            "contexts": [],
            "events": [],
            "meanings": [],
            "query": query
        }
        
        query_lower = query.lower()
        
        # البحث في السياقات
        for ctx in self.memory["contexts"]:
            if query_lower in ctx["text"].lower():
                results["contexts"].append(ctx)
        
        # البحث في الأحداث
        for event in self.memory["events"]:
            if query_lower in event["text"].lower():
                results["events"].append(event)
        
        # البحث في المعاني
        for meaning in self.memory["meanings"]:
            if query_lower in meaning["text"].lower():
                results["meanings"].append(meaning)
        
        # قص النتائج
        results["contexts"] = results["contexts"][:limit]
        results["events"] = results["events"][:limit]
        results["meanings"] = results["meanings"][:limit]
        
        return results

    def get_learned_patterns(self) -> Dict:
        """
        الحصول على الأنماط المتعلمة.
        """
        return self.memory["learned_patterns"]

    def get_strongest_beliefs(self, limit: int = 5) -> List[Dict]:
        """
        الحصول على أقوى المعتقدات المتعلمة.
        """
        meanings = sorted(
            self.memory["meanings"],
            key=lambda x: x.get("strength", 1),
            reverse=True
        )
        return meanings[:limit]

    def get_latest_events(self, limit: int = 10) -> List[Dict]:
        """
        الحصول على آخر الأحداث.
        """
        return self.memory["events"][-limit:]

    def reinforce_meaning(self, meaning_id: int) -> Optional[Dict]:
        """
        تقوية معنى معين (تكراره).
        """
        for meaning in self.memory["meanings"]:
            if meaning["id"] == meaning_id:
                meaning["strength"] += 1
                self.save_to_disk()
                return meaning
        return None

    def export_memory(self, filename: str = "memory_export.json") -> bool:
        """
        تصدير الذاكرة كاملة.
        """
        try:
            export_path = self.data_dir / filename
            with open(export_path, 'w', encoding='utf-8') as f:
                json.dump(self.memory, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"خطأ في التصدير: {e}")
            return False

    def get_statistics(self) -> Dict:
        """
        احصائيات الذاكرة.
        """
        return {
            "total_contexts": len(self.memory["contexts"]),
            "total_events": len(self.memory["events"]),
            "total_meanings": len(self.memory["meanings"]),
            "total_relationships": len(self.memory["relationships"]),
            "patterns_learned": len(self.memory["learned_patterns"]),
            "created_at": self.memory["created_at"],
            "last_update": self.creation_time.isoformat()
        }

    def to_dict(self) -> Dict:
        """
        تحويل مستودع الذاكرة إلى قاموس.
        """
        return {
            "statistics": self.get_statistics(),
            "learned_patterns": self.get_learned_patterns(),
            "strongest_beliefs": self.get_strongest_beliefs(3)
        }

    def __str__(self) -> str:
        stats = self.get_statistics()
        return f"MemoryStore(contexts={stats['total_contexts']}, events={stats['total_events']}, meanings={stats['total_meanings']})"
