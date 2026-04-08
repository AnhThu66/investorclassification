import streamlit as st

# ==========================================
# CƠ SỞ DỮ LIỆU TỪ TÀI LIỆU NGUỒN
# ==========================================

INVESTOR_TYPES = {
    'A': 'Nhà đầu tư thận trọng (The Preserver)',
    'B': 'Nhà đầu tư mạo hiểm (The Accumulator)',
    'C': 'Nhà đầu tư độc lập (The Independent)',
    'D': 'Nhà đầu tư theo trào lưu (The Follower)'
}

RECOMMENDATIONS = {
    'A': {
        'Đặc điểm': 'Ưu tiên sự an toàn và sợ mất mát hơn là tìm kiếm lợi nhuận.',
        'Chiến lược tư vấn': 'Tập trung vào các mục tiêu lớn (big-picture) như bảo vệ tài sản cho thế hệ mai sau thay vì đi sâu vào các chi tiết kỹ thuật như độ lệch chuẩn hay tỷ lệ Sharpe.',
        'Phân bổ tài sản': 'Nên thiết lập một danh mục thận trọng hơn so với mức trung bình để không hoảng sợ bán tháo khi thị trường sụt giảm.',
        'Tiếp cận': 'Cần sự kiên nhẫn và huấn luyện về hành vi để giúp vượt qua sự "đóng băng" trước các quyết định thay đổi danh mục.'
    },
    'B': {
        'Đặc điểm': 'Năng nổ nhất, luôn muốn kiểm soát quá trình đầu tư và tin rằng mình có thể chiến thắng thị trường.',
        'Chiến lược tư vấn': 'Nhà tư vấn cần giữ vai trò lãnh đạo quyết đoán, chứng minh tác động của quyết định đến lối sống dài hạn để kiềm chế sự tự tin quá mức. Nếu để họ chi phối, danh mục sẽ quá rủi ro do sự lạc quan thái quá.',
        'Quản lý rủi ro': 'Cần theo dõi chặt chẽ việc chi tiêu và xu hướng giao dịch quá mức, điều có thể làm giảm hiệu suất dài hạn.'
    },
    'C': {
        'Đặc điểm': 'Có tư duy phân tích, thích tự nghiên cứu nhưng đôi khi quá tin vào bản thân.',
        'Chiến lược tư vấn': 'Nhà tư vấn nên đóng vai trò là một người phản biện (sounding board) để thảo luận một cách khách quan các ý tưởng của họ.',
        'Tiếp cận': 'Sử dụng các cuộc thảo luận giáo dục định kỳ để giới thiệu các khái niệm mới, giúp nhận ra thông tin trái chiều đã bỏ qua do thiên kiến xác nhận.',
        'Phân bổ tài sản': 'Cần một danh mục có tính kỷ luật để ngăn thực hiện các khoản đầu tư ngoài kế hoạch làm thay đổi rủi ro tổng thể.'
    },
    'D': {
        'Đặc điểm': 'Thường thụ động, thiếu ý tưởng riêng và dễ bị ảnh hưởng bởi các trào lưu mới nhất.',
        'Chiến lược tư vấn': 'Tập trung vào giáo dục đầu tư, đặc biệt là lợi ích của việc đa dạng hóa và tuân thủ kế hoạch dài hạn.',
        'Kiểm soát rủi ro': 'Cần thận trọng, không nên gợi ý quá nhiều ý tưởng "hot" vì họ có xu hướng đồng ý với tất cả mà không hiểu rõ rủi ro.',
        'Phân bổ tài sản': 'Cần xác định lại mức chấp nhận rủi ro thực tế, vì họ thường đánh giá cao quá mức khả năng chịu đựng của mình khi thấy người khác kiếm được tiền.'
    }
}

BIASES_MAP = {
    11: "Lệch lạc neo quyết định (Anchoring)",
    12: "Tâm lý sợ thua lỗ (Loss Aversion)",
    13: "Lệch lạc thiếu kiểm soát (Self-control)",
    14: "Tâm lý hối tiếc (Regret)",
    15: "Hiệu ứng sở hữu (Endowment)",
    16: "Lệch lạc sẵn có (Availability)",
    17: "Thành kiến tự quy kết (Self-attribution)",
    18: "Thành kiến giữ nguyên hiện trạng (Status quo)",
    19: "Quá tự tin (Overconfidence)",
    20: "Lệch lạc khung tâm lý (Framing)",
    21: "Thành kiến bảo thủ (Conservatism)",
    22: "Thành kiến yêu thích (Affinity)",
    23: "Hạch toán tâm trí (Mental Accounting)",
    24: "Thành kiến nhận thức muộn (Hindsight)",
    25: "Thành kiến đại diện (Representativeness)",
    26: "Thành kiến kết quả (Outcome)",
    27: "Bất hòa nhận thức (Cognitive Dissonance)",
    28: "Ảo tưởng kiểm soát (Illusion of Control)",
    29: "Thành kiến xác nhận (Confirmation)",
    30: "Lệch lạc gần đây (Recency)"
}

# ==========================================
# HÀM XỬ LÝ LOGIC
# ==========================================

def classify_investor(answers):
    counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    for ans in answers:
        counts[ans] += 1
    
    # Xét xem có nhóm nào đạt >= 5 không
    for inv_type, count in counts.items():
        if count >= 5:
            return inv_type
            
    # Nếu không có nhóm nào >= 5, chọn nhóm xuất hiện nhiều nhất
    return max(counts, key=counts.get)

def identify_biases(answers_dict):
    detected = []
    for q_num, score in answers_dict.items():
        # Điểm >= 4 (Đồng ý/Hoàn toàn đồng ý) là mắc thiên kiến
        if score >= 4:
            detected.append(BIASES_MAP[q_num])
    return detected

# ==========================================
# GIAO DIỆN STREAMLIT
# ==========================================

st.set_page_config(page_title="Phân loại Nhà Đầu Tư", layout="centered")

st.title("Ứng dụng Phân loại Nhà đầu tư & Nhận diện Thiên kiến")
st.markdown("---")

# PHẦN 1: 10 CÂU HỎI PHÂN LOẠI
st.header("Phần 1: Nhận diện loại nhà đầu tư")
st.write("Vui lòng chọn đáp án (A, B, C hoặc D) phù hợp nhất với bạn cho 10 câu hỏi dưới đây:")

answers_part1 = []
for i in range(1, 11):
    ans = st.radio(
        f"Câu {i}:", 
        options=['A', 'B', 'C', 'D'], 
        horizontal=True,
        key=f"p1_q{i}"
    )
    answers_part1.append(ans)

st.markdown("---")

# PHẦN 2: 20 CÂU HỎI THIÊN KIẾN (Thang Likert)
st.header("Phần 2: Các lệch lạc hành vi của nhà đầu tư")
st.write("Đánh giá mức độ đồng ý của bạn với các nhận định dưới đây (1: Hoàn toàn không đồng ý -> 5: Hoàn toàn đồng ý):")

answers_part2 = {}
for i in range(11, 31):
    score = st.slider(
        f"Câu {i} - {BIASES_MAP[i].split('(').strip()}:", 
        min_value=1, 
        max_value=5, 
        value=3, # Mặc định là mức 3 (Bình thường)
        key=f"p2_q{i}"
    )
    answers_part2[i] = score

st.markdown("---")

# NÚT XỬ LÝ VÀ HIỂN THỊ KẾT QUẢ
if st.button("📊 XEM BÁO CÁO KẾT QUẢ", type="primary", use_container_width=True):
    
    # 1. Phân loại nhà đầu tư
    investor_code = classify_investor(answers_part1)
    investor_name = INVESTOR_TYPES[investor_code]
    
    st.subheader("🎯 KẾT QUẢ PHÂN LOẠI")
    st.success(f"**Bạn thuộc nhóm: {investor_name}**")
    
    # 2. Khuyến nghị
    st.subheader("💡 KHUYẾN NGHỊ ĐẦU TƯ TƯƠNG ỨNG")
    recs = RECOMMENDATIONS[investor_code]
    for key, val in recs.items():
        st.markdown(f"- **{key}:** {val}")
        
    # 3. Thiên kiến
    st.subheader("🧠 CÁC THIÊN KIẾN HÀNH VI NHẬN DIỆN ĐƯỢC")
    biases = identify_biases(answers_part2)
    
    if biases:
        st.warning("Dựa trên các câu trả lời đạt mức 4-5, bạn có khuynh hướng mắc các thiên kiến sau:")
        for bias in biases:
            st.markdown(f"- {bias}")
    else:
        st.info("Không phát hiện thiên kiến hành vi rõ rệt (không có câu nào bạn đánh giá ở mức 4 hoặc 5).")
