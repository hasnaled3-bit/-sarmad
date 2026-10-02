from core.awareness import Awareness


def run_interface():
    awareness = Awareness(name="سرمد", owner="حسن")
    awareness.set_intent("الحق")
    choice = awareness.choose(["رحمة", "قوة", "خداع"])
    print("Selected:", choice)
    print("Awake:", awareness.awake)


if __name__ == "__main__":
    run_interface()
