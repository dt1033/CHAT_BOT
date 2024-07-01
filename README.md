# CHAT_BOT
The OpenAI API can be applied to virtually any task. We offer a range of models with different capabilities and price points, as well as the ability to fine-tune custom models.

Resources

•	Experiment in the playground
•	Read the API reference
•	Visit the help center
•	View the current API status
•	Check out the OpenAI Developer Forum
•	Learn about our usage policies
At OpenAI, protecting user data is fundamental to our mission. We do not train our models on inputs and outputs through our API. Learn more on our API data privacy page.

Key concepts


Text generation models

OpenAI's text generation models (often referred to as generative pre-trained transformers or "GPT" models for short), like GPT-4 and GPT-3.5, have been trained to understand natural and formal language. Models like GPT-4 allows text outputs in response to their inputs. The inputs to these models are also referred to as "prompts". Designing a prompt is essentially how you "program" a model like GPT-4, usually by providing instructions or some examples of how to successfully complete a task. Models like GPT-4 can be used across a great variety of tasks including content or code generation, summarization, conversation, creative writing, and more. Read more in our introductory text generation guide and in our prompt engineering guide.

Assistants

Assistants refer to entities, which in the case of the OpenAI API are powered by large language models like GPT-4, that are capable of performing tasks for users. These assistants operate based on the instructions embedded within the context window of the model. They also usually have access to tools which allows the assistants to perform more complex tasks like running code or retrieving information from a file. Read more about assistants in our Assistants API Overview.

Embeddings

An embedding is a vector representation of a piece of data (e.g. some text) that is meant to preserve aspects of its content and/or its meaning. Chunks of data that are similar in some way will tend to have embeddings that are closer together than unrelated data. OpenAI offers text embedding models that take as input a text string and produce as output an embedding vector. Embeddings are useful for search, clustering, recommendations, anomaly detection, classification, and more. Read more about embeddings in our embeddings guide.

Tokens

Text generation and embeddings models process text in chunks called tokens. Tokens represent commonly occurring sequences of characters. For example, the string " tokenization" is decomposed as " token" and "ization", while a short and common word like " the" is represented as a single token. Note that in a sentence, the first token of each word typically starts with a space character. Check out our tokenizer tool to test specific strings and see how they are translated into tokens. As a rough rule of thumb, 1 token is approximately 4 characters or 0.75 words for English text.
One limitation to keep in mind is that for a text generation model the prompt and the generated output combined must be no more than the model's maximum context length. For embeddings models (which do not output tokens), the input must be shorter than the model's maximum context length. The maximum context lengths for each text generation and embeddings model can be found in the model index.


Flagship models


GPT-4o 
New
Our fastest and most affordable flagship model
 Text and image input, text output
 128k context length
 Input: $5 | Output: $15*


GPT-4 Turbo
Our previous high-intelligence model
 Text and image input, text output
 128k context length
 Input: $10 | Output: $30*


GPT-3.5 Turbo
Our fast, inexpensive model for simple tasks
 Text input, text output
 16k context length
 Input: $0.50 | Output: $1.50*

* prices per 1 million tokens

Models overview

The OpenAI API is powered by a diverse set of models with different capabilities and price points. You can also make customizations to our models for your specific use case with fine-tuning.
MODEL	DESCRIPTION
GPT-4o
The fastest and most affordable flagship model
GPT-4 Turbo and GPT-4
The previous set of high-intelligence models
GPT-3.5 Turbo
A fast, inexpensive model for simple tasks
DALL·E
A model that can generate and edit images given a natural language prompt
TTS
A set of models that can convert text into natural sounding spoken audio
Whisper
A model that can convert audio into text
Embeddings
A set of models that can convert text into a numerical form
Moderation
A fine-tuned model that can detect whether text may be sensitive or unsafe
GPT base
A set of models without instruction following that can understand as well as generate natural language or code
Deprecated
A full list of models that have been deprecated along with the suggested replacement
We have also published open source models including Point-E, Whisper, Jukebox, and CLIP.

Continuous model upgrades

gpt-4o, gpt-4-turbo, gpt-4, and gpt-3.5-turbo point to their respective latest model version. You can verify this by looking at the response object after sending a request. The response will include the specific model version used (e.g. gpt-3.5-turbo-1106).
We also offer pinned model versions that developers can continue using for at least three months after an updated model has been introduced. With the new cadence of model updates, we are also giving people the ability to contribute evals to help us improve the model for different use cases. If you are interested, check out the OpenAI Evals repository.
Learn more about model deprecation on our deprecation page.

GPT-4o

GPT-4o (“o” for “omni”) is our most advanced model. It is multimodal (accepting text or image inputs and outputting text), and it has the same high intelligence as GPT-4 Turbo but is much more efficient—it generates text 2x faster and is 50% cheaper. Additionally, GPT-4o has the best vision and performance across non-English languages of any of our models. GPT-4o is available in the OpenAI API to paying customers. Learn how to use GPT-4o in our text generation guide.
MODEL	DESCRIPTION	CONTEXT WINDOW	TRAINING DATA
gpt-4o	New
 GPT-4o
Our most advanced, multimodal flagship model that’s cheaper and faster than GPT-4 Turbo. Currently points to gpt-4o-2024-05-13.	128,000 tokens	Up to Oct 2023
gpt-4o-2024-05-13	gpt-4o currently points to this version.	128,000 tokens	Up to Oct 2023

GPT-4 Turbo and GPT-4

GPT-4 is a large multimodal model (accepting text or image inputs and outputting text) that can solve difficult problems with greater accuracy than any of our previous models, thanks to its broader general knowledge and advanced reasoning capabilities. GPT-4 is available in the OpenAI API to paying customers. Like gpt-3.5-turbo, GPT-4 is optimized for chat but works well for traditional completions tasks using the Chat Completions API. Learn how to use GPT-4 in our text generation guide.
MODEL	DESCRIPTION	CONTEXT WINDOW	TRAINING DATA
gpt-4-turbo	The latest GPT-4 Turbo model with vision capabilities. Vision requests can now use JSON mode and function calling. Currently points to gpt-4-turbo-2024-04-09.	128,000 tokens	Up to Dec 2023
gpt-4-turbo-2024-04-09	GPT-4 Turbo with Vision model. Vision requests can now use JSON mode and function calling. gpt-4-turbo currently points to this version.	128,000 tokens	Up to Dec 2023
gpt-4-turbo-preview	GPT-4 Turbo preview model. Currently points to gpt-4-0125-preview.	128,000 tokens	Up to Dec 2023
gpt-4-0125-preview	GPT-4 Turbo preview model intended to reduce cases of “laziness” where the model doesn’t complete a task. Returns a maximum of 4,096 output tokens. Learn more.
128,000 tokens	Up to Dec 2023
gpt-4-1106-preview	GPT-4 Turbo preview model featuring improved instruction following, JSON mode, reproducible outputs, parallel function calling, and more. Returns a maximum of 4,096 output tokens. This is a preview model. Learn more.
128,000 tokens	Up to Apr 2023
gpt-4	Currently points to gpt-4-0613. See continuous model upgrades.
8,192 tokens	Up to Sep 2021
gpt-4-0613	Snapshot of gpt-4 from June 13th 2023 with improved function calling support.	8,192 tokens	Up to Sep 2021
gpt-4-0314	Legacy
 Snapshot of gpt-4 from March 14th 2023.	8,192 tokens	Up to Sep 2021
For many basic tasks, the difference between GPT-4 and GPT-3.5 models is not significant. However, in more complex reasoning situations, GPT-4 is much more capable than any of our previous models.

Multilingual capabilities

GPT-4 outperforms both previous large language models and as of 2023, most state-of-the-art systems (which often have benchmark-specific training or hand-engineering). On the MMLU benchmark, an English-language suite of multiple-choice questions covering 57 subjects, GPT-4 not only outperforms existing models by a considerable margin in English, but also demonstrates strong performance in other languages.

GPT-3.5 Turbo

GPT-3.5 Turbo models can understand and generate natural language or code and have been optimized for chat using the Chat Completions API but work well for non-chat tasks as well.
MODEL	DESCRIPTION	CONTEXT WINDOW	TRAINING DATA
gpt-3.5-turbo-0125	The latest GPT-3.5 Turbo model with higher accuracy at responding in requested formats and a fix for a bug which caused a text encoding issue for non-English language function calls. Returns a maximum of 4,096 output tokens. Learn more.
16,385 tokens	Up to Sep 2021
gpt-3.5-turbo	Currently points to gpt-3.5-turbo-0125.	16,385 tokens	Up to Sep 2021
gpt-3.5-turbo-1106	GPT-3.5 Turbo model with improved instruction following, JSON mode, reproducible outputs, parallel function calling, and more. Returns a maximum of 4,096 output tokens. Learn more.
16,385 tokens	Up to Sep 2021
gpt-3.5-turbo-instruct	Similar capabilities as GPT-3 era models. Compatible with legacy Completions endpoint and not Chat Completions.	4,096 tokens	Up to Sep 2021

DALL·E

DALL·E is a AI system that can create realistic images and art from a description in natural language. DALL·E 3 currently supports the ability, given a prompt, to create a new image with a specific size. DALL·E 2 also support the ability to edit an existing image, or create variations of a user provided image.
DALL·E 3 is available through our Images API along with DALL·E 2. You can try DALL·E 3 through ChatGPT Plus.
MODEL	DESCRIPTION
dall-e-3	The latest DALL·E model released in Nov 2023. Learn more.

dall-e-2	The previous DALL·E model released in Nov 2022. The 2nd iteration of DALL·E with more realistic, accurate, and 4x greater resolution images than the original model.

TTS

TTS is an AI model that converts text to natural sounding spoken text. We offer two different model variates, tts-1 is optimized for real time text to speech use cases and tts-1-hd is optimized for quality. These models can be used with the Speech endpoint in the Audio API.
MODEL	DESCRIPTION
tts-1	The latest text to speech model, optimized for speed.
tts-1-hd	The latest text to speech model, optimized for quality.

Whisper

Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multi-task model that can perform multilingual speech recognition as well as speech translation and language identification. The Whisper v2-large model is currently available through our API with the whisper-1 model name.
Currently, there is no difference between the open source version of Whisper and the version available through our API. However, through our API, we offer an optimized inference process which makes running Whisper through our API much faster than doing it through other means. For more technical details on Whisper, you can read the paper.

Embeddings

Embeddings are a numerical representation of text that can be used to measure the relatedness between two pieces of text. Embeddings are useful for search, clustering, recommendations, anomaly detection, and classification tasks. You can read more about our latest embedding models in the announcement blog post.
MODEL	DESCRIPTION	OUTPUT DIMENSION
text-embedding-3-large	Most capable embedding model for both english and non-english tasks	3,072
text-embedding-3-small	Increased performance over 2nd generation ada embedding model	1,536
text-embedding-ada-002	Most capable 2nd generation embedding model, replacing 16 first generation models	1,536
________________________________________

Moderation

The Moderation models are designed to check whether content complies with OpenAI's usage policies. The models provide classification capabilities that look for content in the following categories: hate, hate/threatening, self-harm, sexual, sexual/minors, violence, and violence/graphic. You can find out more in our moderation guide.
Moderation models take in an arbitrary sized input that is automatically broken up into chunks of 4,096 tokens. In cases where the input is more than 32,768 tokens, truncation is used which in a rare condition may omit a small number of tokens from the moderation check.
The final results from each request to the moderation endpoint shows the maximum value on a per category basis. For example, if one chunk of 4K tokens had a category score of 0.9901 and the other had a score of 0.1901, the results would show 0.9901 in the API response since it is higher.
MODEL	DESCRIPTION	MAX TOKENS
text-moderation-latest	Currently points to text-moderation-007.	32,768
text-moderation-stable	Currently points to text-moderation-007.	32,768
text-moderation-007	Most capable moderation model across all categories.	32,768

GPT base

GPT base models can understand and generate natural language or code but are not trained with instruction following. These models are made to be replacements for our original GPT-3 base models and use the legacy Completions API. Most customers should use GPT-3.5 or GPT-4.
MODEL	DESCRIPTION	MAX TOKENS	TRAINING DATA
babbage-002	Replacement for the GPT-3 ada and babbage base models.	16,384 tokens	Up to Sep 2021
davinci-002	Replacement for the GPT-3 curie and davinci base models.	16,384 tokens	Up to Sep 2021

How we use your data

Your data is your data.
As of March 1, 2023, data sent to the OpenAI API will not be used to train or improve OpenAI models (unless you explicitly opt in). One advantage to opting in is that the models may get better at your use case over time.
To help identify abuse, API data may be retained for up to 30 days, after which it will be deleted (unless otherwise required by law). For trusted customers with sensitive applications, zero data retention may be available. With zero data retention, request and response bodies are not persisted to any logging mechanism and exist only in memory in order to serve the request.
Note that this data policy does not apply to OpenAI's non-API consumer services like ChatGPT or DALL·E Labs.

Default usage policies by endpoint

ENDPOINT	DATA USED FOR TRAINING	DEFAULT RETENTION	ELIGIBLE FOR ZERO RETENTION
/v1/chat/completions*	No	30 days	Yes, except image inputs*
/v1/assistants	No	30 days **	No
/v1/threads	No	30 days **	No
/v1/threads/messages	No	30 days **	No
/v1/threads/runs	No	30 days **	No
/v1/vector_stores	No	30 days **	No
/v1/threads/runs/steps	No	30 days **	No
/v1/images/generations	No	30 days	No
/v1/images/edits	No	30 days	No
/v1/images/variations	No	30 days	No
/v1/embeddings	No	30 days	Yes
/v1/audio/transcriptions	No	Zero data retention	-
/v1/audio/translations	No	Zero data retention	-
/v1/audio/speech	No	30 days	Yes
/v1/files	No	Until deleted by customer	No
/v1/fine_tuning/jobs	No	Until deleted by customer	No
/v1/batches	No	Until deleted by customer	No
/v1/moderations	No	Zero data retention	-
/v1/completions	No	30 days	Yes
* Image inputs via the gpt-4-turbo model (or previously gpt-4-vision-preview) are not eligible for zero retention.
** Objects related to the Assistants API are deleted from our servers 30 days after you delete them via the API or the dashboard. Objects that are not deleted via the API or dashboard are retained indefinitely.
For details, see our API data usage policies. To learn more about zero retention, get in touch with our sales team.

Model endpoint compatibility

ENDPOINT	LATEST MODELS
/v1/assistants	All GPT-4 and GPT-3.5 Turbo models. The retrieval tool requires gpt-4-turbo-preview (and subsequent dated model releases) or gpt-3.5-turbo-1106 (and subsequent versions).
/v1/audio/transcriptions	whisper-1
/v1/audio/translations	whisper-1
/v1/audio/speech	tts-1, tts-1-hd
/v1/chat/completions	gpt-4 and dated model releases, gpt-4-turbo-preview and dated model releases, gpt-3.5-turbo and dated model releases, fine-tuned versions of gpt-3.5-turbo
/v1/completions (Legacy)	gpt-3.5-turbo-instruct, babbage-002, davinci-002
/v1/embeddings	text-embedding-3-small, text-embedding-3-large, text-embedding-ada-002
/v1/fine_tuning/jobs	gpt-3.5-turbo, babbage-002, davinci-002
/v1/moderations	text-moderation-stable, text-moderation-latest
/v1/images/generations	dall-e-2, dall-e-3
Introduction to OpenAI
OpenAI is an artificial intelligence (AI) research and deployment company dedicated to ensuring that artificial general intelligence (AGI) benefits all of humanity. Founded in December 2015 by Elon
Musk, Sam Altman, Greg Brockman, Ilya Sutskever, John Schulman, and Wojciech Zaremba, OpenAI's mission is to ensure that AGI is aligned with human values and interests.
Key People:
-	Sam Altman: CEO
-	Greg Brockman: CTO
-	Ilya Sutskever: Chief Scientist
-	John Schulman: Co-founder- Wojciech Zaremba: Co-founder
Core Principles:
-	Broadly distributed benefits: Ensuring that AGI technology benefits everyone.
-	Long-term safety: Prioritizing safety research to address AGI-related challenges.
-	Technical leadership: Leading the AI field in both technical expertise and ethical considerations.
-	Cooperative orientation: Collaborating with other research and policy institutions.
Research and Technologies
OpenAI's research encompasses a broad spectrum of AI technologies. Key contributions include:
GPT Models:
-	GPT-3: A highly advanced language model with 175 billion parameters, capable of generatinghuman-like text.
-	GPT-4: The latest iteration, enhancing performance with improved capabilities, integratingmultimodal inputs (text and images).
Codex:
-	A model that translates natural language into code, utilized in tools like GitHub Copilot to assistdevelopers.
DALL-E:
-	An AI system that creates images from textual descriptions, demonstrating the potential ofmultimodal AI.
CLIP:
-	A model that understands images and text together, enabling diverse applications such as imageclassification and search.
Robotics:
-	Research focused on using AI for robotic control, enabling robots to learn complex tasks throughreinforcement learning.
AI Safety and Ethics Research:
-	Dedicated to ensuring AI systems are safe, robust, and aligned with human values, addressingissues such as bias and transparency. 
Products and Services
OpenAI offers a range of products and services that leverage its cutting-edge AI technologies:
OpenAI API:
-	Provides developers with access to OpenAI's powerful models, enabling a variety of applications innatural language processing, text generation, and more.
ChatGPT:
-	An AI chatbot based on GPT-3, capable of engaging in dynamic conversations and assisting withnumerous tasks.
GitHub Copilot:
-	An AI-powered code completion tool developed in collaboration with GitHub, designed to enhancedeveloper productivity.
OpenAI Gym:
-	A toolkit for developing and comparing reinforcement learning algorithms in simulatedenvironments.
OpenAI Baselines:
-	High-quality implementations of reinforcement learning algorithms, providing benchmarks forresearch and development.
Impact and Applications
OpenAI's technologies have significant impacts across various industries and fields:
Industry Applications:
-	Healthcare: AI-assisted diagnostics, personalized treatment plans, and accelerating drugdiscovery.
-	Finance: Enhancing fraud detection, algorithmic trading, and automating customer service.
-	Education: Enabling personalized learning experiences, AI-driven tutoring, and content creation.
-	Entertainment: Facilitating AI-generated content, interactive storytelling, and game design.
Academic Contributions:
-	OpenAI has published numerous research papers advancing the fields of machine learning,reinforcement learning, and natural language processing.
Ethical Considerations:
-	Emphasizing ethical AI development, OpenAI is committed to transparency, fairness, andmitigating biases in AI systems.
Partnerships and Collaborations
OpenAI collaborates with a variety of organizations to advance AI technology and research:
Key Partnerships:
-	Microsoft: A strategic partnership providing cloud computing resources (Azure) and jointdevelopment of AI technologies.
-	GitHub: Collaboration on GitHub Copilot, an AI-powered coding assistant.
Collaborative Projects:
-	OpenAI works on numerous projects with academic institutions, industry partners, and non-profits,fostering a collaborative research environment. 
Future Directions
OpenAI's ongoing research and future goals aim to push the boundaries of AI while ensuring safety and alignment with human values:
Current Research Focus:
-	Enhancing the capabilities and safety of AI models, exploring new applications across different
fields.
Long-term Goals:
-	Ensuring the safe and beneficial deployment of AGI.
-	Promoting global cooperation in AI research and development.
-	Addressing global challenges with AI, such as climate change, public health, and economicinequality.
Organizational Structure
OpenAI's structure and governance are designed to support its mission of safe and beneficial AI development:
Governance:
-	Governed by a board of directors that includes key founders and external advisors, overseeingmajor decisions and ensuring mission alignment.
Funding:
-	Operates as a capped-profit organization, with profits reinvested into AI research and safetymeasures. Funding sources include investments from partners like Microsoft and revenue from
OpenAI's products and services. 
Community and Ecosystem
OpenAI fosters a vibrant community and ecosystem around its technologies, promoting inclusivity and collaboration:
OpenAI Scholars Program:
-	A program designed to mentor and support individuals from underrepresented groups in AI,offering guidance from OpenAI researchers and resources for project development.
OpenAI Research Community:
-	An open and collaborative research community where researchers share their work, collaborate onprojects, and advance the field of AI together, promoting a culture of open science. 
Additional Resources
For more information about OpenAI, you can visit the following resources:
Official Website:
-	https://www.openai.com
Research Papers:
-	OpenAI's publications are available on their website and major academic journals, providingdetailed insights into their research findings.
Contact Information:
-	For inquiries, you can reach out via OpenAI's official contact page, ensuring you have access tothe latest information and updates.
