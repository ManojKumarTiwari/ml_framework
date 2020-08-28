import torch
from torchvision import transforms

def single_img_preprocess(pil_img):
  """
  This function proprocess the PIL image file to feed to Resnet Model.

  Params:
  -------
  pil_img: should be a variable having PIL image.

  Output:
  -------
  returns Image tensor that can be feed to Resnet Model
  """
  preprocess = transforms.Compose([
                                   transforms.Resize(256),
                                   transforms.CenterCrop(224),
                                   transforms.ToTensor(),
                                   transforms.Normalize(
                                       mean=[0.485, 0.456, 0.406],
                                       std=[0.229, 0.224, 0.225]
                                   )
  ])

  img_t = preprocess(pil_img)
  return torch.unsqueeze(img_t, 0) 