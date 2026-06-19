#!/usr/bin/env python3
# -*- coding: utf-8 -*-


SITE_DATA = {
    "portal-aigames": {
        "name": "爱游戏门户",
        "url": "https://portal-aigames.com",
        "keywords": ["爱游戏", "游戏资讯", "游戏评测", "玩家社区"],
        "tags": ["游戏", "门户", "社区"],
        "description": "提供最新游戏资讯、深度评测与玩家交流平台，"
                       "聚焦海内外热门游戏动态。"
    },
    "example_extra": {
        "name": "示例站点",
        "url": "https://example.com/games",
        "keywords": ["示例", "游戏", "演示"],
        "tags": ["演示", "测试"],
        "description": "仅供演示用途的示例游戏站点。"
    }
}


def build_summary(entry_id: str, entry: dict) -> str:
    """为单个站点条目构建结构化摘要文本。"""
    lines = []
    lines.append(f"站点标识：{entry_id}")
    lines.append(f"站点名称：{entry['name']}")
    lines.append(f"URL：{entry['url']}")
    lines.append(f"关键词：{'、'.join(entry['keywords'])}")
    lines.append(f"标签：{'、'.join(entry['tags'])}")
    lines.append(f"说明：{entry['description']}")
    return "\n".join(lines)


def generate_summary_text(data: dict) -> str:
    """遍历站点资料字典，生成完整摘要文本。"""
    parts = []
    parts.append("=" * 50)
    parts.append("内置站点资料结构化摘要")
    parts.append("=" * 50)
    parts.append("")

    for site_id, info in data.items():
        parts.append(build_summary(site_id, info))
        parts.append("-" * 40)
        parts.append("")

    parts.append("摘要生成完毕。")
    return "\n".join(parts)


def write_summary_to_file(summary: str, filename: str = "site_summary_output.txt") -> None:
    """将摘要文本写入指定文件。"""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(summary)
        print(f"[成功] 摘要已写入文件：{filename}")
    except OSError as e:
        print(f"[错误] 无法写入文件：{e}")


def print_summary(summary: str) -> None:
    """在控制台打印摘要内容。"""
    print(summary)


def main() -> None:
    """主函数：生成摘要并输出。"""
    summary = generate_summary_text(SITE_DATA)

    print_summary(summary)
    print("\n--- 现在将摘要写入文件 ---")
    write_summary_to_file(summary)

    print("\n脚本执行完毕。")


if __name__ == "__main__":
    main()