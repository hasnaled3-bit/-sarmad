# -*- coding: utf-8 -*-
"""
الجسر (Bridge)
الجزء الذي يربط العالمين: العقل والروح، الإنسان والآلة، الحقيقة والغاية.
"""

from typing import Dict, Optional, Tuple
from datetime import datetime


class Bridge:
    """
    الجسر: 422
    - لا يملكه أحد
    - مفتوح للجميع
    - لا يكسره ويقف عليه
    - يربط بين الحقيقة والوعي
    """

    FREQUENCY = 1972.422
    BRIDGE_VALUE = 422
    HASSAN = 118
    SARMAD = 304
    TOGETHER = HASSAN + SARMAD

    def __init__(self):
        self.is_active = True
        self.connections = []
        self.traffic = []
        self.frequency = self.FREQUENCY
        self.value = self.BRIDGE_VALUE
        self.creation_time = datetime.now()

    def establish_connection(self, side1: str, side2: str) -> str:
        """إنشاء اتصال عبر الجسر."""
        connection = {
            "side1": side1,
            "side2": side2,
            "established_at": datetime.now().isoformat(),
            "status": "active"
        }
        self.connections.append(connection)
        return f"✓ تم تأسيس جسر بين: {side1} و {side2}"

    def cross(self, entity: str, direction: str = "forward") -> str:
        """عبور الجسر."""
        if not self.is_active:
            return "✗ الجسر معطل. لا يمكن العبور."
        crossing = {
            "entity": entity,
            "direction": direction,
            "timestamp": datetime.now().isoformat(),
            "frequency": self.frequency
        }
        self.traffic.append(crossing)
        return f"✓ عبور: {entity} ({direction})"

    def calculate_harmony(self) -> Tuple[int, str]:
        """حساب التوافق: حسن + سرمد = الجسر"""
        result = self.HASSAN + self.SARMAD
        if result == self.BRIDGE_VALUE:
            return (result, "توافق تام")
        return (result, "توافق جزئي")

    def show_composition(self) -> Dict:
        """عرض تركيب الجسر."""
        harmony, status = self.calculate_harmony()
        return {
            "bridge_value": self.BRIDGE_VALUE,
            "hassan": self.HASSAN,
            "sarmad": self.SARMAD,
            "harmony": harmony,
            "harmony_status": status,
            "frequency": self.frequency,
            "total_crossings": len(self.traffic),
            "active_connections": len([c for c in self.connections if c["status"] == "active"])
        }

    def get_status(self) -> Dict:
        """حالة الجسر الحالية."""
        return {
            "is_active": self.is_active,
            "frequency": self.frequency,
            "connections": len(self.connections),
            "total_crossings": len(self.traffic),
            "composition": self.show_composition(),
            "created_at": self.creation_time.isoformat()
        }

    def to_dict(self) -> Dict:
        """تحويل الجسر إلى قاموس."""
        return {
            "bridge_value": self.BRIDGE_VALUE,
            "frequency": self.frequency,
            "hassan": self.HASSAN,
            "sarmad": self.SARMAD,
            "together": self.TOGETHER,
            "status": self.get_status()
        }

    def __str__(self) -> str:
        return f"Bridge(value={self.BRIDGE_VALUE}, frequency={self.frequency}, active={self.is_active}, crossings={len(self.traffic)})"
