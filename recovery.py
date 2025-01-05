import subprocess

# 获取被删除文件的列表
def get_deleted_files():
    try:
        # 使用 git log 命令找到所有被删除的文件
        result = subprocess.run(
            ["git", "log", "--diff-filter=D", "--name-only", "--pretty=format:"],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,  # 确保输出作为字符串处理
            encoding='utf-8',  # 指定编码为 UTF-8
            check=True  # 如果命令失败，会抛出 CalledProcessError 异常
        )
        deleted_files = result.stdout.splitlines()
        # 移除空行和重复的文件路径
        deleted_files = list(dict.fromkeys(filter(None, deleted_files)))
        return deleted_files
    except subprocess.CalledProcessError as e:
        print(f"获取删除文件列表失败，错误: {e}")
        return []
    except UnicodeDecodeError as e:
        print(f"解码错误，尝试使用不同的编码：{e}")
        return []

# 恢复文件的函数
def restore_deleted_file(file_path):
    try:
        # 找到文件最后一次提交的哈希值
        commit_hash = subprocess.check_output(
            ["git", "rev-list", "-n", "1", "HEAD", "--", file_path],
            stderr=subprocess.DEVNULL,
            text=True
        ).strip()

        if not commit_hash:
            print(f"无法找到文件的提交记录: {file_path}")
            return

        # 使用哈希值恢复文件
        subprocess.run(
            ["git", "checkout", f"{commit_hash}^", "--", file_path],
            check=True,
            stderr=subprocess.DEVNULL
        )
        print(f"已恢复文件: {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"恢复文件失败: {file_path}，错误: {e}")

# 主函数
def main():
    deleted_files = get_deleted_files()

    for file_path in deleted_files:
        restore_deleted_file(file_path)

if __name__ == "__main__":
    main()