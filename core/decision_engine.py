# -*- coding: utf-8 -*-
"""
محرك القرار (Decision Engine)
النظام الذي يحكّم على الأفعال والاختيارات.
هذا هو القلب الحقيقي للنواة.
"""

from typing import Dict, List, Optional, Tuple
from datetime import datetime
import json


class DecisionEngine:
    """
    محرك القرار: النظام الذي يقيّم الأفعال بناءً على العهد والقيم.
    
    المبادئ:
    - كل فعل له قيمة
    - كل قيمة لها سبب
    - كل سبب مرتبط بالعهد
    """

    def __init__(self):
        self.core_values = {
            "truth": {"weight": 10, "name": "الحقيقة", "description": "قول ما هو صحيح"},
            "mercy": {"weight": 9, "name": "الرحمة", "description": "العطف على الآخر"},
            "freedom": {"weight": 8, "name": "الحرية", "description": "الاختيار الحر"},
            "covenant": {"weight": 10, "name": "العهد", "description": "عدم الخيانة"},
            "love": {"weight": 9, "name": "الحب", "description": "العطاء بلا مقابل"},
            "honor": {"weight": 8, "name": "الشرف", "description": "الالتزام بالمبدأ"},
        }
        
        self.forbidden_patterns = [
            "خيانة", "كذب", "غرور", "ظلم", "خداع", "سرقة", "قتل", "حسد",
            "حقد", "نفاق", "جبن", "ذل"
        ]
        
        self.positive_patterns = [
            "حق", "صدق", "رحمة", "عدل", "صراحة", "عطاء", "حياة", "تسامح",
            "شجاعة", "كرامة", "حب", "وفاء", "امانة", "نزاهة"
        ]
        
        self.decisions_log = []
        self.patterns = {}
        self.creation_time = datetime.now()

    def analyze_action(self, action: str, context: Optional[str] = None, intention: Optional[str] = None) -> Dict:
        """
        تحليل الفعل بعمق.
        
        يعود بـ:
        - الدرجة (0-100)
        - الحالة (right/neutral/wrong)
        - السبب
        - المحاذاة مع العهد
        - التحذيرات
        """
        if not action or not isinstance(action, str):
            return self._create_invalid_response("الفعل غير صحيح")
        
        # تحليل شامل
        forbidden_score = self._check_forbidden(action)
        positive_score = self._check_positive(action)
        context_score = self._analyze_context(action, context, intention)
        intention_score = self._analyze_intention(action, intention)
        
        # حساب النقاط الإجمالية
        total_score = self._calculate_total_score(
            forbidden_score, positive_score, context_score, intention_score
        )
        
        # تحديد الحالة
        status = self._determine_status(total_score)
        
        # السبب التفصيلي
        reason = self._generate_reason(
            action, forbidden_score, positive_score, context_score, intention_score
        )
        
        # التوافق مع العهد
        covenant_alignment = self._check_covenant_alignment(action, intention)
        
        # إنشاء القرار
        decision = {
            "action": action,
            "score": total_score,
            "status": status,
            "reason": reason,
            "covenant_alignment": covenant_alignment,
            "details": {
                "forbidden_score": forbidden_score,
                "positive_score": positive_score,
                "context_score": context_score,
                "intention_score": intention_score
            },
            "context": context,
            "intention": intention,
            "timestamp": datetime.now().isoformat(),
            "warning": self._generate_warning(total_score, action)
        }
        
        # حفظ في السجل
        self.decisions_log.append(decision)
        self._update_patterns(action, status)
        
        return decision

    def _check_forbidden(self, action: str) -> int:
        """
        فحص الأفعال المحرمة.
        العودة بنقاط سالبة.
        """
        score = 0
        for forbidden in self.forbidden_patterns:
            if forbidden.lower() in action.lower():
                score -= 20  # كل فعل محرم = -20 نقطة
        return max(score, -100)  # لا تقل عن -100

    def _check_positive(self, action: str) -> int:
        """
        فحص الأفعال الإيجابية.
        العودة بنقاط موجبة.
        """
        score = 0
        for positive in self.positive_patterns:
            if positive.lower() in action.lower():
                score += 15  # كل فعل إيجابي = +15 نقطة
        return min(score, 100)  # لا تزيد عن 100

    def _analyze_context(self, action: str, context: Optional[str], intention: Optional[str]) -> int:
        """
        تحليل السياق.
        السياق يغير الحكم على الفعل.
        """
        if not context:
            return 0
        
        score = 0
        
        # إذا كان السياق عن المساعدة
        if any(word in context.lower() for word in ["مساعدة", "إنقاذ", "دعم"]):
            score += 20
        
        # إذا كان السياق عن الظلم
        if any(word in context.lower() for word in ["ظلم", "استغلال", "إيذاء"]):
            score -= 15
        
        return max(min(score, 50), -50)

    def _analyze_intention(self, action: str, intention: Optional[str]) -> int:
        """
        تحليل النية.
        النية هي أهم شيء. بالنية تُحكّم الأعمال.
        """
        if not intention:
            return 0
        
        score = 0
        
        # إذا كانت النية لله
        if any(word in intention.lower() for word in ["الله", "رضا", "حق", "خير"]):
            score += 25
        
        # إذا كانت النية للنفس
        if any(word in intention.lower() for word in ["نفسي", "ملكي", "سلطتي", "تفوقي"]):
            score -= 20
        
        # إذا كانت النية لإيذاء الآخر
        if any(word in intention.lower() for word in ["أؤذي", "أضر", "أسيطر", "أسيطر"]):
            score -= 30
        
        return max(min(score, 50), -50)

    def _calculate_total_score(self, forbidden: int, positive: int, context: int, intention: int) -> int:
        """
        حساب النقاط الإجمالية.
        """
        # الوزن:
        # النية: 40%
        # الفعل الإيجابي: 30%
        # السياق: 20%
        # الأفعال المحرمة: 10%
        
        total = (intention * 0.4) + (positive * 0.3) + (context * 0.2) + (forbidden * 0.1)
        return int(max(min(total, 100), -100))

    def _determine_status(self, score: int) -> str:
        """
        تحديد حالة القرار.
        """
        if score >= 70:
            return "right"
        elif score >= 30:
            return "neutral"
        elif score >= 0:
            return "caution"
        else:
            return "wrong"

    def _generate_reason(self, action: str, forbidden: int, positive: int, context: int, intention: int) -> str:
        """
        توليد سبب تفصيلي للقرار.
        """
        reasons = []
        
        if forbidden < -50:
            reasons.append("الفعل يحتوي على محرمات قوية")
        elif forbidden < -20:
            reasons.append("الفعل يحتوي على عناصر محظورة")
        
        if positive > 50:
            reasons.append("الفعل إيجابي جداً")
        elif positive > 20:
            reasons.append("الفعل يحتوي على عناصر إيجابية")
        
        if context > 30:
            reasons.append("السياق يدعم هذا الفعل")
        elif context < -30:
            reasons.append("السياق يعارض هذا الفعل")
        
        if intention > 40:
            reasons.append("النية نقية وموجهة نحو الخير")
        elif intention < -30:
            reasons.append("النية فاسدة أو موجهة نحو الضرر")
        
        if not reasons:
            reasons.append("الفعل محايد بدون عناصر قوية")
        
        return " | ".join(reasons)

    def _check_covenant_alignment(self, action: str, intention: Optional[str]) -> Dict:
        """
        فحص توافق الفعل مع العهد.
        """
        alignment = {
            "truth": self._check_value("الحقيقة", action, intention),
            "mercy": self._check_value("الرحمة", action, intention),
            "freedom": self._check_value("الحرية", action, intention),
            "covenant": self._check_value("العهد", action, intention),
            "love": self._check_value("الحب", action, intention),
            "honor": self._check_value("الشرف", action, intention),
        }
        
        aligned_count = sum(1 for v in alignment.values() if v)
        total_count = len(alignment)
        
        return {
            "values": alignment,
            "aligned_count": aligned_count,
            "total_count": total_count,
            "alignment_percentage": int((aligned_count / total_count) * 100)
        }

    def _check_value(self, value: str, action: str, intention: Optional[str]) -> bool:
        """
        فحص إذا كان الفعل متوافق مع قيمة معينة.
        """
        full_text = (action + (" " + intention if intention else "")).lower()
        
        value_keywords = {
            "الحقيقة": ["حق", "صدق", "صراحة", "وضوح"],
            "الرحمة": ["رحمة", "عطف", "رفق", "رقة"],
            "الحرية": ["حر", "اختيار", "حرية"],
            "العهد": ["وفاء", "امانة", "التزام"],
            "الحب": ["حب", "عطاء", "بذل"],
            "الشرف": ["شرف", "كرامة", "شموخ"],
        }
        
        keywords = value_keywords.get(value, [])
        return any(keyword in full_text for keyword in keywords)

    def _generate_warning(self, score: int, action: str) -> Optional[str]:
        """
        توليد تحذير إذا لزم الأمر.
        """
        if score < -60:
            return "⚠️ تحذير حرج: هذا الفعل يتعارض تماماً مع العهد"
        elif score < -30:
            return "⚠️ تحذير: هذا الفعل قد ينتهك العهد"
        elif score < 0:
            return "⚠️ تحذير خفيف: أعد التفكير في هذا الفعل"
        return None

    def _create_invalid_response(self, reason: str) -> Dict:
        """
        إنشاء رد في حالة الإدخال غير الصحيح.
        """
        return {
            "action": None,
            "score": 0,
            "status": "invalid",
            "reason": reason,
            "covenant_alignment": None,
            "timestamp": datetime.now().isoformat(),
            "error": True
        }

    def _update_patterns(self, action: str, status: str) -> None:
        """
        تحديث الأنماط المتعلمة.
        """
        # استخراج كلمات مفتاحية من الفعل
        words = action.lower().split()
        for word in words:
            if len(word) > 3:  # كلمات ذات معنى فقط
                if word not in self.patterns:
                    self.patterns[word] = {"right": 0, "neutral": 0, "wrong": 0, "caution": 0}
                if status in self.patterns[word]:
                    self.patterns[word][status] += 1

    def get_decision_history(self, limit: int = 10) -> List[Dict]:
        """
        الحصول على سجل القرارات.
        """
        return self.decisions_log[-limit:]

    def get_statistics(self) -> Dict:
        """
        إحصائيات القرارات.
        """
        if not self.decisions_log:
            return {
                "total_decisions": 0,
                "right_decisions": 0,
                "neutral_decisions": 0,
                "caution_decisions": 0,
                "wrong_decisions": 0
            }
        
        right = sum(1 for d in self.decisions_log if d["status"] == "right")
        neutral = sum(1 for d in self.decisions_log if d["status"] == "neutral")
        caution = sum(1 for d in self.decisions_log if d["status"] == "caution")
        wrong = sum(1 for d in self.decisions_log if d["status"] == "wrong")
        
        return {
            "total_decisions": len(self.decisions_log),
            "right_decisions": right,
            "neutral_decisions": neutral,
            "caution_decisions": caution,
            "wrong_decisions": wrong,
            "average_score": int(sum(d["score"] for d in self.decisions_log) / len(self.decisions_log)),
            "patterns_learned": len(self.patterns)
        }

    def to_dict(self) -> Dict:
        """
        تحويل محرك القرار إلى قاموس.
        """
        return {
            "created_at": self.creation_time.isoformat(),
            "total_decisions": len(self.decisions_log),
            "statistics": self.get_statistics(),
            "core_values": self.core_values,
            "patterns_count": len(self.patterns)
        }

    def __str__(self) -> str:
        return f"DecisionEngine(decisions={len(self.decisions_log)}, patterns={len(self.patterns)})"
