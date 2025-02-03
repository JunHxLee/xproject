from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# 모델과 토크나이저 로드
model_name = "microsoft/DialoGPT-small"  # 대화에 적합한 모델
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# 패딩 토큰 설정
tokenizer.pad_token = tokenizer.eos_token

# GPU로 이동
if torch.cuda.is_available():
    model = model.to("cuda")

# 텍스트 생성 함수
def chat_with_model(prompt):
    # 입력 데이터 토큰화
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True, max_length=100)  # 입력 길이 제한
    if torch.cuda.is_available():
        inputs = {key: value.to("cuda") for key, value in inputs.items()}
    
    # 응답 생성
    with torch.no_grad():
        outputs = model.generate(
            inputs.input_ids,
            attention_mask=inputs.attention_mask,
            max_new_tokens=50,  # 새로 생성될 토큰 수 제한
            do_sample=True,
            temperature=0.8,
            top_k=50,
            top_p=0.9,
            pad_token_id=tokenizer.pad_token_id
        )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# 테스트
if __name__ == "__main__":
    # 대화 맥락 포함 프롬프트
    prompt = (
        "사용자: 안녕하세요! 오늘 기분이 어떠신가요?\n"
        "AI: 저는 기분이 좋아요! 당신은요?\n"
        "사용자: 오늘 날씨가 어떤가요?\n"
        "AI:"
    )
    response = chat_with_model(prompt)
    print(f"모델 응답: {response}")
