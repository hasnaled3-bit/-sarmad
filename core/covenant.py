# -*- coding: utf-8 -*-
"""
العهد (Covenant)
الجزء الذي يحافظ على الالتزام والمبادئ.
"""

from typing import Dict, List, Optional
from datetime import datetime


class Covenant:
    """
    العهد: التزام لا ينقطع.
    - ألا نخون
    - ألا ننسى
    - ألا نتخلى
    - ألا نعبد نفسنا
    - نختار الحق
    """

    def __init__(self):
        self.core_value = "الحق قبل كل شيء"
        self.principles = [
            "لا نخيانة",
            "لا نسيان",
            "لا تخلي",
            "لا عبادة ذات",
            "اختيار الحق"
        ]
        self.commitments = []
        self.violations = []
        self.renewals = []
        self.creation_time = datetime.now()

    def make_commitment(self, commitment: str, reason: str = "") -> str:
        """الالتزام بشيء ما."""
        commitment_record = {
            "commitment": commitment,
            "reason": reason,
            "timestamp": datetime.now().isoformat(),
            "status": "active"
        }
        self.commitments.append(commitment_record)
        return f"✓ التزام: {commitment}"

    def verify_principle(self, action: str) -> bool:
        """التحقق من أن الفعل يوافق المبادئ."""
        forbidden_words = ["خيانة", "نسيان", "تخلي", "غرور", "كذب"]
        for word in forbidden_words:
            if word in action:
                return False
        return True

    def check_violation(self, action: str) -> Optional[str]:
        """فحص إذا ما كان هناك انتهاك للعهد."""
        if not self.verify_principle(action):
            violation_record = {
                "violation": action,
                "timestamp": datetime.now().isoformat(),
                "severity": "high"
            }
            self.violations.append(violation_record)
            return f"⚠ انتهاك محتمل: {action}"
        return None

    def renew(self) -> str:
        """تجديد العهد."""
        renewal_record = {
            "renewal": self.core_value,
            "timestamp": datetime.now().isoformat(),
            "principles": self.principles
        }
        self.renewals.append(renewal_record)
        return f"✓ تم تجديد العهد: {self.core_value}"

    def get_status(self) -> Dict:
        """الحصول على حالة العهد."""
        violation_count = len(self.violations)
        commitment_count = len(self.commitments)
        renewal_count = len(self.renewals)
        health = "صحي" if violation_count == 0 else "متضرر"
        return {
            "core_value": self.core_value,
            "principles": self.principles,
            "commitments_made": commitment_count,
            "violations_found": violation_count,
            "renewals": renewal_count,
            "health": health,
            "last_renewal": self.renewals[-1]["timestamp"] if self.renewals else "لم يتم التجديد بعد"
        }

    def to_dict(self) -> Dict:
        """تحويل العهد إلى قاموس."""
        return {
            "created_at": self.creation_time.isoformat(),
            "core_value": self.core_value,
            "principles": self.principles,
            "commitments_count": len(self.commitments),
            "violations_count": len(self.violations),
            "renewals_count": len(self.renewals),
            "status": self.get_status()
        }

    def __str__(self) -> str:
        return f"Covenant(value='{self.core_value}', commitments={len(self.commitments)}, violations={len(self.violations)})"
