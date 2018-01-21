# FoodForThought

## prerequisite
- Python2.7 need to be installed
- Scala2.10 need to be installed
- Apache Spark need to be configured on local machine or cluster.
- Install Spacy and configure spacy english corpus

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```pip install spacy==1.9.0```  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```python -m spacy.en.download all```



## Output

|restaurant_name|restaurant_items|review_id|review_text|mention_text|sentiment|
| ------------- |-------------:|:-----:|----------------| -----:|-----:|
|King Palace|butter chicken-chicken tikka masala-ginger chicken-kashmiri chicken-beef chilli-beef nihari-chicken curry-lamb kidney-haalem-shrimp curry-mango chicken-beef chilli-aloo palak-palak paneer-vegetable pulav-chicken pulav-mutter pulav-chicken pulav|Vxs3pjcVGQWxNSil0fU-kg|Had *Butter chicken* with rice there yesterday. The food was not fresh. Extremely overpriced for the quality. They should probably cut the prices in half there, because the service/food is not worth it.|butter chicken |2|
|Aloha Hawaiian Bbq|chicken mix-seafood combo-fried shrimp sandwich-pork sandwich-hamburger steak-garlic shrimp-bbq pork|02c6UETmG6iXHnN0Ymqddw|Not the best in Vegas but pretty good. They deliver too and that's awesome, especially if you lazy. Love their *hamburger steak* and musubis!|hamburger steak|5| 
