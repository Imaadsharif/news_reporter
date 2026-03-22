from src.orchestrator import run_pipeline

def main():
    print("📰 Multi-Agent News System (CLI)")
    print("Type 'exit' to quit\n")

    while True:
        topic = input("Enter news topic: ").strip()

        if topic.lower() == "exit":
            print("Exiting...")
            break

        try:
            result = run_pipeline(topic)

            print("\n🔍 Research:\n")
            print(result["research"])

            print("\n📌 Summary:\n")
            print(result["summary"])

            print("\n📰 Final Output:\n")
            print(result["final"])

            print("\n" + "="*60)

        except Exception as e:
            print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()