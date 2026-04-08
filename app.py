import streamlit as st

# Thiết lập giao diện
st.set_page_config(page_title="Phân loại Nhà đầu tư & Hành vi", layout="wide")

st.title("Phân loại Loại hình Nhà đầu tư & Lệch lạc Hành vi 📈")
st.write("Dựa trên nghiên cứu về Tài chính hành vi (Behavioral Finance)")

# --- PHẦN 1: NHẬN DIỆN LOẠI NHÀ ĐẦU TƯ ---
st.header("Phần 1: Nhận diện loại nhà đầu tư")
st.info("Hãy chọn phương án mô tả đúng nhất về bạn trong 10 câu hỏi sau.")

questions = [
    "1. Vai trò chính của Anh/Chị trong việc quản lý tiền bạc là:",
    "2. Khi nói đến các vấn đề tài chính, Anh/Chị đồng ý nhất với nhận định nào?",
    "3. Khi quyết định đầu tư, Anh/Chị tin tưởng vào lời khuyên của:",
    "4. Khi thị trường đi lên, Anh/Chị cảm thấy:",
    "5. Trong lĩnh vực tài chính, từ nào mô tả đúng nhất về Anh/Chị?",
    "6. Về việc tuân thủ một kế hoạch quản lý tiền bạc:",
    "7. Anh/Chị cảm thấy tự tin nhất về tiền bạc khi:",
    "8. Khi một người bạn gợi ý một ý tưởng đầu tư 'chắc ăn':",
    "9. Biến động ngắn hạn trong danh mục khiến Anh/Chị:",
    "10. Nếu tham gia một trận đá bóng, Anh/Chị đóng vai trò nào?"
]

options = [
    ["Người bảo vệ tài sản (A)", "Tích cực giao dịch (B)", "Nghiên cứu kỹ lưỡng (C)", "Nghe theo lời khuyên (D)"],
    ["Mất tiền là kết quả tồi tệ nhất (A)", "Hành động nhanh để kiếm cơ hội (B)", "Dành thời gian nghiên cứu kỹ (C)", "Không trực tiếp giám sát tiền (D)"],
    ["Kỷ luật tự giác (A)", "Bản năng của mình (B)", "Kết quả nghiên cứu riêng (C)", "Một người khác (D)"],
    ["Nhẹ nhõm (A)", "Phấn khích (B)", "Bình tĩnh và lý trí (C)", "Vui vì làm theo lời khuyên (D)"],
    ["Người bảo vệ (Guardian) (A)", "Người giao dịch (Trader) (B)", "Người nghiên cứu (Researcher) (C)", "Người nghe theo lời khuyên (D)"],
    ["Làm nếu giúp bảo vệ tài sản (A)", "Kế hoạch không quá quan trọng (B)", "Kế hoạch tốt nhưng cần suy nghĩ riêng (C)", "Nghe theo lời khuyên người khác (D)"],
    ["Ngủ ngon vì tài sản an toàn (A)", "Đầu tư tiềm năng tăng giá cao (B)", "Tự đưa ra quyết định (C)", "Đầu tư theo đám đông (D)"],
    ["Thường tránh những loại này (A)", "Yêu thích và hành động ngay (B)", "Tự nghiên cứu rồi mới quyết định (C)", "Hỏi ý kiến người khác (D)"],
    ["Hoảng sợ và muốn bán (A)", "Thấy cơ hội và muốn mua (B)", "Bình tĩnh, kiểm soát được (C)", "Muốn gọi hỏi xem tiền thế nào (D)"],
    ["Cầu thủ phòng ngự (A)", "Cầu thủ tấn công (B)", "Chiến lược gia/Huấn luyện viên (C)", "Người hâm mộ (D)"]
]

responses = []
for i in range(len(questions)):
    choice = st.selectbox(questions[i], options[i], key=f"q{i}")
    responses.append(choice[-2]) # Lấy ký tự A, B, C hoặc D

# --- PHẦN 2: LỆCH LẠC HÀNH VI ---
st.divider()
st.header("Phần 2: Nhận diện lệch lạc hành vi")
st.write("Bạn có đồng ý với các nhận định sau không?")

bias_questions = [
    "11. Khi định bán một khoản đầu tư, giá tôi đã mua là yếu tố lớn tôi cân nhắc.",
    "12. Nỗi đau mất tiền mạnh gấp ít nhất 2 lần niềm vui kiếm được tiền.",
    "13. Tôi sẽ mua những thứ mình muốn ngay cả khi chúng không phải lựa chọn tài chính tốt nhất.",
    "14. Những quyết định tài chính sai lầm trong quá khứ khiến tôi thay đổi quyết định hiện tại.",
    "17. Tôi thấy các đầu tư thành công là do tôi, còn thất bại là do lời khuyên người khác.",
    "19. Tôi tin rằng kiến thức đầu tư của mình trên mức trung bình.",
    "29. Khi đầu tư không tốt, tôi tìm thông tin để xác nhận rằng mình đã quyết định đúng."
]
bias_types = ["Anchoring (Neo quyết định)", "Loss Aversion (Sợ thua lỗ)", "Self-control (Thiếu kiểm soát)", "Regret (Hối tiếc)", "Self-attribution (Tự quy kết)", "Overconfidence (Quá tự tin)", "Confirmation (Xác nhận)"]

bias_results = []
for i in range(len(bias_questions)):
    agree = st.checkbox(bias_questions[i])
    if agree:
        bias_results.append(bias_types[i])

# --- XỬ LÝ KẾT QUẢ ---
if st.button("XEM KẾT QUẢ PHÂN LOẠI"):
    st.divider()
    
    # Tính toán loại nhà đầu tư
    count_A = responses.count('A')
    count_B = responses.count('B')
    count_C = responses.count('C')
    count_D = responses.count('D')
    
    # Xác định nhóm
    if count_A >= 5:
        loai = "Nhà đầu tư Thận trọng (The Preserver)"
        kn = """
        - **Chiến lược:** Tập trung bảo vệ tài sản cho thế hệ mai sau thay vì các chỉ số kỹ thuật[cite: 4, 5].
        - **Tiếp cận:** Cần sự kiên nhẫn và huấn luyện hành vi để vượt qua sự 'đóng băng' quyết định[cite: 6].
        """
    elif count_B >= 5:
        loai = "Nhà đầu tư Mạo hiểm (The Accumulator)"
        kn = """
        - **Chiến lược:** Nhà tư vấn cần giữ vai trò lãnh đạo quyết đoán để kiềm chế sự lạc quan thái quá[cite: 9, 10].
        - **Quản lý rủi ro:** Theo dõi chặt chẽ việc chi tiêu và xu hướng giao dịch quá mức[cite: 12].
        """
    elif count_C >= 5:
        loai = "Nhà đầu tư Độc lập (The Independent)"
        kn = """
        - **Chiến lược:** Nhà tư vấn đóng vai trò người phản biện khách quan cho các ý tưởng của bạn[cite: 15].
        - **Tiếp cận:** Cần kỷ luật để tránh các khoản đầu tư ngoài kế hoạch[cite: 17].
        """
    elif count_D >= 5:
        loai = "Nhà đầu tư Theo trào lưu (The Follower)"
        kn = """
        - **Chiến lược:** Tập trung giáo dục về đa dạng hóa và tuân thủ kế hoạch dài hạn[cite: 20].
        - **Kiểm soát rủi ro:** Xác định lại mức chấp nhận rủi ro thực tế thay vì chạy theo đám đông[cite: 22].
        """
    else:
        loai = "Nhà đầu tư Hỗn hợp"
        kn = "Bạn có đặc điểm của nhiều nhóm. Hãy tham vấn chuyên gia để có danh mục tối ưu."

    # Hiển thị kết quả
    st.subheader(f"Kết quả: {loai}")
    st.markdown(kn)
    
    if bias_results:
        st.warning("⚠️ Cảnh báo Thiên kiến (Biases) bạn đang gặp phải:")
        for b in bias_results:
            st.write(f"- {b}")
    else:
        st.success("Bạn có tư duy khá khách quan và ít bị ảnh hưởng bởi thiên kiến hành vi.")
