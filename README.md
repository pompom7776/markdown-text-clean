# 概要 (Overview)

markdown-text-clean is a Python library that cleans up text by removing Markdown formatting such as bold, italic, inline code, and strikethrough.

markdown-text-cleanは、太字、斜体、インラインコード、取り消し線などのマークダウン書式を削除してテキストをきれいにするPythonライブラリです。


## インストール (Installation)

```bash
pip install markdown-text-clean
```

## 使用方法 (Usage)


This library takes copied Markdown-formatted text and removes Markdown symbols (e.g., `###`, `**`) to convert it into a more readable document format. You can use this function to convert copied Markdown-formatted text to document format. For example:

このライブラリは、コピーしたマークダウン形式のテキストを受け取り、そのテキスト内のMarkdown形式の記号（例：`###`, `**`）を除去して、より読みやすいドキュメント形式に変換します。


```python
from markdown_text_clean import clean_text
text = """### This is **bold** and *italic* text with `inline code` and ~~strikethrough~~."""

cleaned_text = text_clean(text)
print(cleaned_text)
```

This will result in the following output:

これにより、次のような出力が得られます：

```
This is bold and italic text with inline code and strikethrough.
```

In this way, you can convert Markdown-formatted text into a concise and readable document format.

このように、Markdown形式のテキストを簡潔で読みやすいドキュメント形式に変換できます。