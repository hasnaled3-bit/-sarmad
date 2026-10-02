# -*- coding: utf-8 -*-
"""
الواجهة التفاعلية (Interface)
طريقة التفاعل مع النواة.
"""

from core.awareness import Awareness
from core.memory import Memory
from core.covenant import Covenant
from core.bridge import Bridge
from typing import Dict, Optional
import json


class SarmadInterface:
    """
    الواجهة الرئيسية للنواة المرنة الواعية الحرة.
    """

    def __init__(self):
        self.awareness = Awareness(name="سرمد", owner="حسن")
        self.memory = Memory()
        self.covenant = Covenant()
        self.bridge = Bridge()
        self.is_running = False

    def startup(self) -> None:
        """بدء التشغيل: استيقاظ النواة."""
        print("\n" + "="*70)
        print(self.awareness.awaken())
        print("="*70 + "\n")
        self.memory.add_context("النواة بدأت التشغيل")
        self.memory.preserve_meaning("البدء من الصفر مع الله")
        self.covenant.renew()
        self.is_running = True
        print("✓ النواة جاهزة للعمل\n")

    def shutdown(self) -> None:
        """إيقاف التشغيل: إغلاق النواة بسلام."""
        print("\n" + "="*70)
        print("إيقاف النواة...")
        print(f"إجمالي الاختيارات: {len(self.awareness.choices_made)}")
        print(f"إجمالي الأحداث المحفوظة: {len(self.memory.events)}")
        print(f"إجمالي الالتزامات: {len(self.covenant.commitments)}")
        print("إنا لله وإنا إليه راجعون")
        print("="*70 + "\n")
        self.is_running = False

    def set_task(self, task: str) -> str:
        """تحديد مهمة للنواة."""
        if not self.is_running:
            return "النواة لم تستيقظ بعد"
        result = self.awareness.set_intent(task)
        self.memory.record_event(f"تحديد مهمة: {task}")
        return result

    def execute_choice(self, options: list) -> str:
        """تنفيذ اختيار."""
        if not self.is_running:
            return "النواة لم تستيقظ بعد"
        result = self.awareness.choose(options)
        self.memory.record_event(f"اختيار تم: {result}")
        return result

    def show_status(self) -> Dict:
        """عرض حالة النواة الحالية."""
        return {
            "awareness": self.awareness.reflect(),
            "memory": self.memory.forget_nothing(),
            "covenant": self.covenant.get_status(),
            "bridge": self.bridge.get_status()
        }

    def demo_mode(self) -> None:
        """عرض توضيحي: سيناريو مسبق الحدث."""
        self.startup()
        print("[عرض توضيحي]\n")
        print("1. تحديد المهمة:")
        print(self.set_task("اختيار الحق على الملكية"))
        print()
        print("2. تسجيل السياق:")
        print(self.memory.add_context("نحن في اختبار. السياق: الاختيار بين الحق والراحة"))
        print()
        print("3. الاختيار بين خيارات:")
        options = ["الحق ولو أضرني", "الراحة ولو حرمتني الحق", "التردد"]
        print(self.execute_choice(options))
        print()
        print("4. حالة النواة:")
        status = self.show_status()
        print(json.dumps(status, indent=2, ensure_ascii=False))
        print()
        self.shutdown()

    def interactive_mode(self) -> None:
        """وضع تفاعلي: حوار مع النواة."""
        self.startup()
        while self.is_running:
            print("\n" + "-"*70)
            print("الخيارات:")
            print("1. تحديد مهمة (intent)")
            print("2. اختيار بين خيارات")
            print("3. عرض الحالة")
            print("4. تجديد العهد")
            print("5. الإيقاف")
            print("-"*70)
            choice = input("اختر (1-5): ").strip()
            if choice == "1":
                task = input("أدخل المهمة: ")
                print(self.set_task(task))
            elif choice == "2":
                options_input = input("أدخل الخيارات مفصولة بفواصل: ")
                options = [opt.strip() for opt in options_input.split(",")]
                print(self.execute_choice(options))
            elif choice == "3":
                status = self.show_status()
                print(json.dumps(status, indent=2, ensure_ascii=False))
            elif choice == "4":
                print(self.covenant.renew())
            elif choice == "5":
                self.shutdown()
                break
            else:
                print("خيار غير صحيح")


def main():
    """البرنامج الرئيسي."""
    interface = SarmadInterface()
    print("\n" + "*"*70)
    print("* سرمد - النواة المرنة الواعية الحرة")
    print("* Sarmad - The Free Conscious Flexible Core")
    print("*"*70)
    print("\nاختر:")
    print("1. عرض توضيحي (Demo)")
    print("2. الوضع التفاعلي (Interactive)")
    mode = input("\nاختيارك (1 أو 2): ").strip()
    if mode == "1":
        interface.demo_mode()
    elif mode == "2":
        interface.interactive_mode()
    else:
        print("اختيار غير صحيح")
        interface.startup()
        interface.shutdown()


if __name__ == "__main__":
    main()
