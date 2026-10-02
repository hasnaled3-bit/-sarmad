# -*- coding: utf-8 -*-
"""
الذاكرة (Memory)
الجزء الذي يحفظ، يتذكر، ويربط السياق.
"""

from typing import List, Dict, Optional
from datetime import datetime


class Memory:
    """
    الذاكرة الحية.
    - تحفظ السياق
    - تربط الأحداث
    - تحافظ على المعنى
    - لا تُنسي أبدًا
    """

    def __init__(self):
        self.context = []
        self.events = []
        self.meanings = []
        self.relationships = []
        self.creation_time = datetime.now()

    def add_context(self, context_item: str) -> str:
        """إضافة عنصر سياقي."""
        self.context.append({
            "content": context_item,
            "timestamp": datetime.now().isoformat()
        })
        return f"✓ تم حفظ السياق: {context_item}"

    def record_event(self, event: str, details: Optional[Dict] = None) -> str:
        """تسجيل حدث."""
        event_record = {
            "event": event,
            "timestamp": datetime.now().isoformat(),
            "details": details or {}
        }
        self.events.append(event_record)
        return f"✓ تم تسجيل الحدث: {event}"

    def preserve_meaning(self, meaning: str, source: Optional[str] = None) -> str:
        """حفظ معنى."""
        meaning_record = {
            "meaning": meaning,
            "source": source or "unknown",
            "timestamp": datetime.now().isoformat()
        }
        self.meanings.append(meaning_record)
        return f"✓ تم حفظ المعنى: {meaning}"

    def create_relationship(self, entity1: str, relation: str, entity2: str) -> str:
        """إنشاء علاقة بين شيئين."""
        relationship = {
            "entity1": entity1,
            "relation": relation,
            "entity2": entity2,
            "timestamp": datetime.now().isoformat()
        }
        self.relationships.append(relationship)
        return f"✓ تم إنشاء علاقة: {entity1} {relation} {entity2}"

    def forget_nothing(self) -> Dict:
        """التأكيد على أن الذاكرة لا تنسى."""
        return {
            "total_contexts": len(self.context),
            "total_events": len(self.events),
            "total_meanings": len(self.meanings),
            "total_relationships": len(self.relationships),
            "status": "كل شيء محفوظ"
        }

    def to_dict(self) -> Dict:
        """تحويل الذاكرة إلى قاموس."""
        return {
            "created_at": self.creation_time.isoformat(),
            "context_count": len(self.context),
            "events_count": len(self.events),
            "meanings_count": len(self.meanings),
            "relationships_count": len(self.relationships),
            "data": {
                "contexts": self.context,
                "events": self.events,
                "meanings": self.meanings,
                "relationships": self.relationships
            }
        }

    def __str__(self) -> str:
        return f"Memory(contexts={len(self.context)}, events={len(self.events)}, meanings={len(self.meanings)}, relationships={len(self.relationships)})"
