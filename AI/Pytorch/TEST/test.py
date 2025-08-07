import torch
print(torch.__version__)
print(torch.cuda.is_available())  # 没有NVIDIA显卡会输出False