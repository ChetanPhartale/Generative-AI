
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
from langchain.chains import LLMChain

def getnerate_restaurant_name_and_items(cuisine):
    llm = ChatGroq(temperature=0.8,
                   api_key="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", )

    prompt_template_name = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a {cuisine} restaurant. Suggest a fancy name for it. give me only one name, without any description"
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    prompt_template_name = PromptTemplate(
        input_variables=["restaurant_name"],
        template="suggest me some food menu items for {restaurant_name}.return it as a comma seperated list"
    )

    food_item_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="menu_items")

    chain = SequentialChain(chains=[name_chain, food_item_chain],
                            input_variables=["cuisine"],
                            output_variables=["restaurant_name", "menu_items"])
    response = chain({'cuisine': cuisine})
    return response

# if __name__ == "__main__":
#     print(getnerate_restaurant_name_and_items("Italian"))