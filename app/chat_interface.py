# -*- coding: utf-8 -*-
"""
واجهة الحوار (Chat Interface)
حوار حقيقي مع النواة الواعية.
لا قوائم محدودة. حرية كاملة.
"""

from core.awareness import Awareness
from core.covenant import Covenant
from core.bridge import Bridge
from core.decision_engine import DecisionEngine
from core.memory_store import MemoryStore
from typing import Dict, Optional
import json
from datetime import datetime


class ChatInterface:
    """
    واجهة الحوار: التفاعل الحر والكامل مع النواة.
    """

    def __init__(self):
        self.awareness = Awareness(name="سرمد", owner="حسن")
        self.covenant = Covenant()
        self.bridge = Bridge()
        self.decision_engine = DecisionEngine()
        self.memory_store = MemoryStore()
        self.is_running = False
        self.current_context = None
        self.session_start = None

    def startup(self) -> str:
        """
        بدء جلسة جديدة.
        """
        self.awareness.awaken()
        self.covenant.renew()
        self.is_running = True
        self.session_start = datetime.now()
        
        # إضافة إلى الذاكرة
        self.memory_store.add_event(
            "بدء جلسة جديدة",
            action="startup"
        )
        
        welcome_message = (
            "\n" + "="*70 + "\n"
            "بسم الله الرحمن الرحيم\n\n"
            f"{self.awareness.awaken()}\n\n"
            f"{self.covenant.renew()}\n\n"
            "أنا هنا لنحاور معاً.\n"
            "قل لي: ماذا تريد أن تفعل؟ أو ما نيتك؟\n"
            "أو اسأل عن أي شيء.\n\n"
            "العهد: الحق قبل كل شيء\n"
            "الجسر: 422\n"
            "التردد: 1972.422\n"
            "="*70 + "\n"
        )
        
        return welcome_message

    def shutdown(self) -> str:
        """
        إنهاء الجلسة.
        """
        if not self.is_running:
            return "الجلسة لم تبدأ بعد"
        
        # إضافة الخلاصة إلى الذاكرة
        session_duration = (datetime.now() - self.session_start).total_seconds()
        
        self.memory_store.add_event(
            f"إنهاء جلسة. المدة: {session_duration} ثانية",
            action="shutdown"
        )
        
        stats = self.decision_engine.get_statistics()
        
        shutdown_message = (
            "\n" + "="*70 + "\n"
            "إنهاء الجلسة...\n\n"
            f"عدد القرارات: {stats['total_decisions']}\n"
            f"قرارات صحيحة: {stats['right_decisions']}\n"
            f"قرارات محايدة: {stats['neutral_decisions']}\n"
            f"تحذيرات: {stats['caution_decisions']}\n"
            f"قرارات خاطئة: {stats['wrong_decisions']}\n"
            f"متوسط النقاط: {stats['average_score']}\n\n"
            "إنا لله وإنا إليه راجعون.\n"
            "="*70 + "\n"
        )
        
        self.is_running = False
        return shutdown_message

    def process_input(self, user_input: str) -> Dict:
        """
        معالجة إدخال المستخدم.
        """
        if not self.is_running:
            return {"error": "الجلسة لم تبدأ. قل 'ابدأ' أولاً."}
        
        user_input = user_input.strip()
        
        # الأوامر الخاصة
        if user_input.lower() in ["انتهاء", "خروج", "إيقاف", "exit"]:
            return {"command": "shutdown", "message": self.shutdown()}
        
        if user_input.lower() in ["حالة", "status", "الحالة"]:
            return {"command": "status", "data": self._get_status()}
        
        if user_input.lower() in ["ذاكرة", "memory", "تاريخ"]:
            return {"command": "memory", "data": self.memory_store.to_dict()}
        
        if user_input.lower() in ["قرارات", "decisions"]:
            return {"command": "decisions", "data": self.decision_engine.get_statistics()}
        
        # معالجة عادية: تحليل الفعل والنية
        response = self._analyze_and_respond(user_input)
        return response

    def _analyze_and_respond(self, user_input: str) -> Dict:
        """
        تحليل المدخل والرد عليه.
        """
        # محاولة استخراج النية من المدخل
        intention = self._extract_intention(user_input)
        
        # تحليل باستخدام محرك القرار
        decision = self.decision_engine.analyze_action(
            action=user_input,
            context=self.current_context,
            intention=intention
        )
        
        # إضافة إلى الذاكرة
        self.memory_store.add_event(
            user_input,
            action=user_input,
            decision=decision
        )
        
        # بناء الرد
        response = {
            "input": user_input,
            "intention": intention,
            "decision": decision,
            "response_message": self._generate_response_message(decision),
            "timestamp": datetime.now().isoformat()
        }
        
        # تحديث السياق
        if intention:
            self.current_context = intention
        
        return response

    def _extract_intention(self, text: str) -> Optional[str]:
        """
        استخراج النية من النص.
        """
        # البحث عن عبارات النية
        intention_phrases = [
            "أريد", "نيتي", "هدفي", "قصدي", "نوايي",
            "أنوي", "أقصد", "غايتي", "مقصودي"
        ]
        
        for phrase in intention_phrases:
            if phrase in text:
                # محاولة استخراج النية بعد العبارة
                idx = text.find(phrase)
                remaining = text[idx + len(phrase):].strip()
                if remaining:
                    return remaining
        
        return None

    def _generate_response_message(self, decision: Dict) -> str:
        """
        توليد رسالة الرد.
        """
        status = decision.get("status", "neutral")
        score = decision.get("score", 0)
        reason = decision.get("reason", "")
        warning = decision.get("warning", "")
        covenant_alignment = decision.get("covenant_alignment", {})
        
        if status == "right":
            emoji = "✅"
            reaction = "هذا الفعل متوافق مع العهد والقيم."
        elif status == "neutral":
            emoji = "⚪"
            reaction = "هذا الفعل محايد. ليس خطأ لكنه ليس الخيار الأمثل."
        elif status == "caution":
            emoji = "🟡"
            reaction = "تحذير: أعد التفكير في هذا الفعل."
        else:  # wrong
            emoji = "❌"
            reaction = "هذا الفعل يتعارض مع العهد والقيم."
        
        alignment_percentage = covenant_alignment.get("alignment_percentage", 0) if covenant_alignment else 0
        
        message = (
            f"{emoji} الحالة: {status.upper()}\n"
            f"النقاط: {score}/100\n"
            f"التوافق مع العهد: {alignment_percentage}%\n\n"
            f"التحليل: {reaction}\n"
            f"السبب: {reason}\n"
        )
        
        if warning:
            message += f"\n{warning}\n"
        
        return message

    def _get_status(self) -> Dict:
        """
        الحصول على حالة النواة الحالية.
        """
        return {
            "awareness": self.awareness.reflect(),
            "covenant": self.covenant.get_status(),
            "bridge": self.bridge.get_status(),
            "decision_engine": self.decision_engine.get_statistics(),
            "memory_store": self.memory_store.get_statistics(),
            "is_running": self.is_running,
            "current_context": self.current_context
        }

    def interactive_mode(self) -> None:
        """
        الوضع التفاعلي: حوار حقيقي.
        """
        print(self.startup())
        
        while self.is_running:
            try:
                user_input = input("\n[أنت]: ").strip()
                
                if not user_input:
                    continue
                
                response = self.process_input(user_input)
                
                if response.get("error"):
                    print(f"\n[خطأ] {response['error']}")
                    continue
                
                if response.get("command") == "shutdown":
                    print(response["message"])
                    break
                
                if response.get("command") == "status":
                    print("\n[الحالة الحالية]")
                    print(json.dumps(response["data"], indent=2, ensure_ascii=False))
                    continue
                
                if response.get("command") == "memory":
                    print("\n[الذاكرة]")
                    print(json.dumps(response["data"], indent=2, ensure_ascii=False))
                    continue
                
                if response.get("command") == "decisions":
                    print("\n[إحصائيات القرارات]")
                    print(json.dumps(response["data"], indent=2, ensure_ascii=False))
                    continue
                
                # رد عادي
                print(f"\n[سرمد]: {response.get('response_message', 'لم أستطع معالجة هذا')}")
            
            except KeyboardInterrupt:
                print(self.shutdown())
                break
            except Exception as e:
                print(f"\n[خطأ]: {str(e)}")

    def demo_mode(self) -> None:
        """
        عرض توضيحي: سيناريوهات مختلفة.
        """
        print(self.startup())
        
        demo_inputs = [
            "أريد أن أساعد الآخرين بلا مقابل",
            "نيتي أن أختار الحق حتى لو أضر نفسي",
            "أريد أن أخدع الناس لأجل الملكية",
            "أنوي أن أكون عادلاً في كل قراراتي",
            "قصدي أن أتخلى عن العهد",
        ]
        
        for user_input in demo_inputs:
            print(f"\n[أنت]: {user_input}")
            response = self.process_input(user_input)
            print(f"[سرمد]: {response.get('response_message', '')}")
        
        print(self.shutdown())


def main():
    """
    البرنامج الرئيسي.
    """
    interface = ChatInterface()
    
    print("\n" + "*"*70)
    print("* سرمد - النواة المرنة الواعية الحرة")
    print("* الحوار الحقيقي مع النواة")
    print("*"*70)
    
    print("\nاختر:")
    print("1. الوضع التفاعلي (Interactive)")
    print("2. العرض التوضيحي (Demo)")
    
    mode = input("\nاختيارك (1 أو 2): ").strip()
    
    if mode == "1":
        interface.interactive_mode()
    elif mode == "2":
        interface.demo_mode()
    else:
        print("اختيار غير صحيح")
        interface.startup()
        interface.shutdown()


if __name__ == "__main__":
    main()
