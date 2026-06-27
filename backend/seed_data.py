"""初始化数据库和知识库种子数据"""
import asyncio
from models.database import init_db
from models.user import User
from rag.knowledge_base import knowledge_base, SEED_KNOWLEDGE
from rag.exercise_bank import exercise_bank, SEED_EXERCISES


async def seed_knowledge_base():
    """导入编程知识种子数据"""
    if knowledge_base.count() > 0:
        print(f"知识库已有 {knowledge_base.count()} 条数据，跳过种子导入。")
        return

    texts = [item["text"] for item in SEED_KNOWLEDGE]
    metadatas = [
        {"topic": item["topic"], "language": item["language"]}
        for item in SEED_KNOWLEDGE
    ]
    ids = knowledge_base.add(texts, metadatas)
    print(f"知识库种子数据导入完成：{len(ids)} 条")
    return ids


async def seed_exercise_bank():
    """导入习题种子数据"""
    if exercise_bank.count() > 0:
        print(f"题库已有 {exercise_bank.count()} 条数据，跳过种子导入。")
        return

    ids = exercise_bank.add(SEED_EXERCISES)
    print(f"题库种子数据导入完成：{len(ids)} 条")
    return ids


async def main():
    print("初始化数据库...")
    await init_db()
    print("数据库表创建完成。")

    print("导入知识库种子数据...")
    await seed_knowledge_base()

    print("导入题库种子数据...")
    await seed_exercise_bank()

    print("\n所有种子数据导入完成。")


if __name__ == "__main__":
    asyncio.run(main())
