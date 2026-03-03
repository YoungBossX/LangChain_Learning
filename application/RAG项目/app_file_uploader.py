import streamlit as st
from knowledge_base import KnowledgeBaseService

# 页面配置
st.set_page_config(
    page_title="RAG 知识库管理",
    page_icon="📚",
    layout="wide"
)

# 初始化 session_state
if "service" not in st.session_state:
    st.session_state["service"] = KnowledgeBaseService()


def extract_text(uploaded_file):
    """根据文件类型提取文本"""
    file_name = uploaded_file.name
    suffix = file_name.rsplit(".", 1)[-1].lower()

    if suffix == "txt":
        return uploaded_file.read().decode("utf-8")
    elif suffix == "md":
        return uploaded_file.read().decode("utf-8")
    elif suffix == "csv":
        return uploaded_file.read().decode("utf-8")
    elif suffix == "json":
        return uploaded_file.read().decode("utf-8")
    else:
        return None

# 主页面
st.title("📚 知识库更新服务")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    uploaded_file = st.file_uploader(
        "请上传文件",
        type=["txt", "md", "csv", "json"],
        accept_multiple_files=False,
        help="支持 TXT、Markdown、CSV、JSON文件"
    )

with col2:
    st.markdown("### 📋 支持的文件格式")
    st.markdown("""
    | 格式 | 说明 |
    |------|------|
    | `.txt` | txt 文件 |
    | `.md` | Markdown 文件 |
    | `.csv` | CSV 表格文件 |
    | `.json` | JSON 数据文件 |
    """)

# 处理上传
if uploaded_file is not None:
    file_name = uploaded_file.name
    text = extract_text(uploaded_file)

    if text is None:
        st.error(f"❌ 不支持的文件格式: {file_name}")
    elif len(text.strip()) == 0:
        st.warning("⚠️ 文件内容为空")
    else:
        with st.expander("📄 预览文件内容", expanded=False):
            st.text(text[:500] + ("..." if len(text) > 500 else ""))
            st.caption(f"文件名: {file_name} | 总字符数: {len(text)}")

        if st.button("✅ 确认上传到知识库", type="primary"):
            with st.spinner("正在处理文件，请稍候..."):
                try:
                    result = st.session_state["service"].upload_by_str(text, file_name)
                    if "[跳过]" in result:
                        st.warning(f"⚠️ {result}")
                    elif "[成功]" in result:
                        st.success(f"🎉 {result}")
                except Exception as e:
                    st.error(f"❌ 上传失败: {e}")