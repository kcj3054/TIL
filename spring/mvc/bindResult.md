#### bindResult란? 

1. BindingResult bindingResult 파라미터의 위치는 @ModelAttribute Item item 다음에 와야 한다
이유는 ModelAttribute item을 bindingResult에 담기 때문이다. 



if (!StringUtils.hasText(item.getItemName())) {
bindingResult.addError(new FieldError("item", "itemName", "상품 이름은

필드에 에러가 있으면 FieldeError 객체를 생성해서 bindingResult에 담아둔다
