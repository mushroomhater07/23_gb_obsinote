import os

def generate_summary_md(directory):
    summary_md = ""
    currentpath = ""
    for path, endpoint, filesArr in os.walk(directory):
        for file in filesArr:
            if file.endswith(".md"):
                if(currentpath != path):
                    currentpath = path
                    if len(path.split(os.sep)) > 1:
                        summary_md += f"\t"         # simple file-system can disable it       
                        summary_md += f"* [{path.split(os.sep)[-1].lower().replace(os.sep, '/')}]({path.replace(' ','-')[2:].replace(os.sep, '/')}/README.md)\n"
                    else:
                        summary_md += f"* [{path.split(os.sep)[-1][2:].lower().replace(os.sep, '/')}]({path.replace(' ','-')[2:].replace(os.sep, '/')}/README.md)\n"
                if(path != directory):
                    # for i in path[len(directory):].split(os.sep):
                    summary_md += f"\t"
                summary_md += f"* [{file[0:-3].lower().replace(os.sep, '/')}](<{os.path.join(path, file)[2:].replace(os.sep, '/')}>)\n"

    with open("SUMMARY.md", "w", encoding="utf-8") as f:
        f.write("# Table of contents\n\n"+summary_md[0:])

    return "SUMMARY.md"


if __name__ == "__main__":
    directory = "./"
    summary_md = generate_summary_md(directory)

    print(f"Generated summary.md file at {summary_md}")
