import os
import shutil
import re

def update_news_files(directory):
    # Match files like announcement_k.md
    pattern = re.compile(r"announcement_(\d+)\.md")

    # List and extract matched filenames and their numbers
    files = [f for f in os.listdir(directory) if pattern.match(f)]
    indexed_files = [(int(pattern.match(f).group(1)), f) for f in files]

    # Sort by descending index to avoid overwriting
    indexed_files.sort(reverse=True)

    # Rename files from k to k+1
    for k, filename in indexed_files:
        src = os.path.join(directory, filename)
        dst = os.path.join(directory, f"announcement_{k + 1}.md")
        os.rename(src, dst)
        print(f"Renamed {filename} -> announcement_{k + 1}.md")

    # Copy announcement_2.md to announcement_1.md
    src_file = os.path.join(directory, "announcement_2.md")
    dst_file = os.path.join(directory, "announcement_1.md")
    shutil.copyfile(src_file, dst_file)
    print("Copied announcement_2.md -> announcement_1.md")

if __name__ == "__main__":
    news_dir = "_news"
    update_news_files(news_dir)
