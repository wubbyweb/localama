from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OllamaEmbeddings
import ollama
import chromadb


def createembeddings(collectionname='my_embeddings',path='doc/transactions.csv'):
    chroma_client = chromadb.PersistentClient(path='./db')
    # Create or get a collection
    collection = chroma_client.get_or_create_collection(name=collectionname)

    # # Load and preprocess your document
    with open(path,encoding='utf-8', mode='r') as file:
        text = file.read()

    # # Split the text into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_text(text)


    for i,t in enumerate(texts):
        embeddings_response = ollama.embeddings(
            model='nomic-embed-text', 
            prompt=t
            )
        embeddings = embeddings_response["embedding"]
        collection.add(
            ids=[str(i)],
            embeddings=[embeddings],
            documents=[t]
        )



#vectorstore = Chroma.from_texts(texts, embeddings)

def infer(collectionname='my_embeddings',query="Summarize the context"):

    chroma_client = chromadb.PersistentClient(path='./db')
    # Set up the Ollama model
    llm = Ollama(base_url='http://127.0.0.1:11434',
                model="phi3")

    rtv_embeddings = OllamaEmbeddings(
        model='nomic-embed-text'
    )

    vectorstore = Chroma(
        client=chroma_client,
        collection_name=collectionname,
        embedding_function=rtv_embeddings
    )

    retriever = vectorstore.as_retriever()

    # Create the RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever
    )

    # Query the model
    print('Inferencing Response...')
    response = qa_chain.invoke(query)
    print(response) 

if __name__ == "__main__":
    createembeddings('auto','doc/auto.txt')
    infer(collectionname='pms',query='Summaries the content')
   