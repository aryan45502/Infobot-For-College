# from flask import Flask, render_template, request, jsonify
# import speech_recognition as sr
# import google.generativeai as genai
# import pygame
# from gtts import gTTS
# import io
# import os

# app = Flask(__name__)

# class AI_Assistant:
#     def __init__(self):
#         genai.configure(api_key='AIzaSyAIGpQ_3eawfsmYoBi-RPpq6H3Dohp5Eco')
#         self.model = genai.GenerativeModel("gemini-pro")
#         self.chat = self.model.start_chat(history=[])
#         self.recognizer = sr.Recognizer()
#         self.full_transcript = []
#         pygame.mixer.init()
#         self.predefined_qa = {
#             "what is your name": "My name is Jack, your virtual assistant.",
#             "how are you feeling today": "I am just a bunch of code, but I am here to help!",
#             "requirement process": "Generally, students need to have completed their higher secondary education (10+2) or equivalent with a minimum specified percentage. Specific programs may have additional requirements, such as a background in science for IT or engineering courses.",
#             "admission process": "Completed application form Academic transcripts and certificates Passport-sized photographs Identification proof (citizenship or passport) Entrance exam scorecard",
#             "entrance": "Yes, Softwarica College often requires an entrance exam for admission, particularly for competitive programs. The format typically includes multiple-choice questions covering subjects relevant to the chosen program.",
#             "fee": "The fee structure varies by program. Detailed fee information is usually provided on the college’s official website or can be obtained from the admissions office.",
#             "scholarship": "Scholarships based on merit and need are available. Scholarships are often awarded to students with excellent academic performance or those in financial need.",
#             "ratio": "This ratio can vary but is generally designed to ensure personalized attention and support for students.",
#             "class": "We typically have moderate class sizes, allowing for interactive learning environments.",
#             "intern": "Opportunities for research and internships are available, often facilitated through partnerships with industries and organizations.",
#             "library": "The college provides a well-stocked library with academic books, journals, and digital resources.",
#             "lab": "Equipped with the latest technology and software to support IT and engineering students.",
#             "sport": "Facilities for various sports, including basketball, football, and indoor games, are available.",
#             "canteen": "We provide the best quality of food services which is affordable.",
#             "club": "Various student clubs and societies for cultural, academic, and recreational activities.",
#             "event": "Regular events, including festivals, sports meets, and competitions, are organized.",
#             "volunteer": "You can participate in different events and be a volunteer.",
#             "leader": "Students can participate in leadership roles within clubs, student councils, and other organizations.",
#             "career": "Career counseling, job placement support, and workshops are provided to assist students in career planning.",
#             "tour": "Organized to provide practical exposure and experiential learning.",
#             "job fairs": "Yes, we organize job fairs each semester where students can meet potential employers and learn about job opportunities.",
#             "address": "Softwarica College of IT is located at Dillibazar, Kathmandu.",
#             "courses": "We have courses of BSc (Hons) Computing, BSc (Hons) Ethical Hacking and Cybersecurity, BSc (Hons) Computer Science with Artificial Intelligence",
#             "enroll now": "That's great! Which course would you like to enroll in?",
#             "faculty": "Both faculty from Science and Management can admit in this college and proceed with their study in IT.",
#             "apply": "You can apply online through our official website or visit our admissions office for assistance with the application process.",
#             "documents": "You will need to submit a completed application form, academic transcripts and certificates, passport-sized photographs, and identification proof.",
#             "semester start": "The semester typically starts in September. For exact dates, please check our academic calendar on the official website and app.",
#             "class timings": "Classes are typically held from 9 AM to 4 PM, but the schedule may vary depending on the program and course.",
#             "admission deadline": "The admission deadlines vary by program. Please check our website or contact the admissions office for the specific deadlines for your chosen program.",
#             "transportation options": "There are several transportation options including public buses, and parking facilities for students who drive.",
#             "abroad study": "Yes, we have study abroad programs that allow students to gain international experience. We also provide international trip for enthusiastic students.",
#             "part-time job": "Yes, there are part-time job opportunities available on campus for students. Please visit our career services office for more information.",
#             "canteen": "We offer a variety of dining options including canteen, coffee shops, and food courts that cater to different dietary preferences.",
#             "graduation requirements": "Graduation requirements vary by program but generally include completing a specified number of credits, passing required courses, and maintaining a minimum GPA.",
#             "refund": "Our refund policy varies by program and circumstance. Admission fees will be refunded with decrease 20% but not the tuition fees",
#             "student attendance": "Regular attendance is expected from all students. Attendance policies is that every student should have above 80% mandatory.",
#             "news and events": "You can stay updated with college news and events by visiting our official app and website, following our social media channels.",
#             "industry professionals": "We organize events such as guest lectures, industry panels, and networking sessions with professionals to help students connect with industry leaders and potential employers.",
#             "तपाई कस्तो हुनुहुन्छ": "म कोडको एउटा गुच्छा मात्र हुँ, तर म तपाईलाई मद्दत गर्न यहाँ छु!",
#             "कलेजमा भर्ना": "थप विवरणहरूको लागि तपाईंलाई परामर्श कोठामा जान अनुरोध गरिन्छ।",
#             "खेलकुद": "बास्केटबल, फुटबल, र इनडोर खेलहरू सहित विभिन्न खेलहरूका लागि सुविधाहरू उपलब्ध छन्।",
#             "भर्ना": "सामान्यतया, विद्यार्थीहरूले आफ्नो उच्च माध्यमिक शिक्षा (10+2) वा न्यूनतम निर्दिष्ट प्रतिशतको साथ बराबर पूरा गरेको हुनुपर्छ। विशिष्ट कार्यक्रमहरूमा अतिरिक्त आवश्यकताहरू हुन सक्छन्, जस्तै IT वा इन्जिनियरिङ पाठ्यक्रमहरूको लागि विज्ञानमा पृष्ठभूमि।",
#             "भर्ना प्रक्रिया": "भरिएको आवेदन फारम शैक्षिक ट्रान्सक्रिप्ट र प्रमाणपत्रहरू पासपोर्ट आकारका फोटोहरू पहिचान प्रमाण (नागरिकता वा राहदानी) प्रवेश परीक्षा स्कोरकार्ड। विद्यार्थीले Softwarica मा भर्नाको लागि आफ्नो +2 प्रमाणपत्र ल्याउनु पर्छ।",
#             "प्रवेश": "हो, Softwarica कलेजले प्राय: भर्नाको लागि प्रवेश परीक्षा चाहिन्छ, विशेष गरी प्रतिस्पर्धी कार्यक्रमहरूको लागि। ढाँचामा सामान्यतया छनोट गरिएको कार्यक्रमसँग सान्दर्भिक विषयहरू समावेश गर्ने बहु-छनोट प्रश्नहरू समावेश हुन्छन्।",
#             "छात्रवृत्ति": "योग्यता र आवश्यकतामा आधारित छात्रवृत्तिहरू उपलब्ध छन्। छात्रवृत्ति प्रायः उत्कृष्ट शैक्षिक प्रदर्शन वा वित्तीय आवश्यकता भएका विद्यार्थीहरूलाई प्रदान गरिन्छ।",
#             "कक्षा": "हामीसँग सामान्यतया मध्यम वर्गको आकार हुन्छ, जसले अन्तरक्रियात्मक सिकाइ वातावरणको लागि अनुमति दिन्छ।",
#             "इन्टर्नशिप": "अनुसन्धान र इन्टर्नशिपका लागि अवसरहरू उपलब्ध छन्, प्रायः उद्योगहरू र संस्थाहरूसँग साझेदारीको माध्यमबाट सहज बनाइन्छ।",
#             "शुल्क": "शुल्क संरचना कार्यक्रम अनुसार फरक हुन्छ। विस्तृत शुल्क जानकारी सामान्यतया कलेजको आधिकारिक वेबसाइटमा प्रदान गरिन्छ वा प्रवेश कार्यालयबाट प्राप्त गर्न सकिन्छ।",
#             "lab": "IT र ईन्जिनियरिङ् विद्यार्थीहरूलाई सहयोग गर्न नवीनतम प्रविधि र सफ्टवेयरले सुसज्जित।",
#             "भ्रमण": "व्यावहारिक एक्सपोजर र अनुभवात्मक शिक्षा प्रदान गर्न संगठित। पहिलो सेमेस्टरका विद्यार्थीहरूलाई २ दिनको भ्रमणमा लगिनेछ र अन्तिम सेमेस्टरका विद्यार्थीहरूलाई पनि भ्रमणमा लगिनेछ।",
#             "पाठ्यक्रमहरू": "हामीसँग बीएससी (ऑनर्स) कम्प्युटिङ, बीएससी (ऑनर्स) एथिकल ह्याकिङ र साइबरसेक्युरिटी, आर्टिफिसियल इन्टेलिजेन्सको साथ बीएससी (ऑनर्स) कम्प्युटर साइन्सका पाठ्यक्रमहरू छन्।",
#             "ठेगाना": "सफ्टवारिका कलेज अफ आईटी डिल्लीबजार, काठमाडौंमा अवस्थित छ।",
#             "भर्ना गर्नुहोस्": "यो राम्रो छ! तपाई कुन पाठ्यक्रममा भर्ना हुन चाहनुहुन्छ?",
#             "संकाय": "विज्ञान र व्यवस्थापन दुबै संकायले यस कलेजमा भर्ना गर्न सक्छन् र आईटीमा आफ्नो अध्ययन जारी राख्न सक्छन्।",
#             "अनुप्रयोग": "तपाईं हाम्रो आधिकारिक वेबसाइटमार्फत अनलाइन आवेदन दिन सक्नुहुन्छ वा आवेदन प्रक्रियाको साथ सहयोगको लागि हाम्रो भर्ना कार्यालयमा जान सक्नुहुन्छ।",
#             "प्रवेश प्रक्रिया": "तपाईंलाई पूरा आवेदन फारम, शैक्षिक ट्रान्सक्रिप्ट र प्रमाणपत्रहरू, पासपोर्ट आकारका फोटोहरू, र पहिचान प्रमाण पेश गर्न आवश्यक हुनेछ।",
#             "सेमेस्टर सुरु": "सेमेस्टर सामान्यतया सेप्टेम्बरमा सुरु हुन्छ। ठ्याक्क मितिहरूको लागि, कृपया हाम्रो आधिकारिक वेबसाइटमा शैक्षिक क्यालेन्डर जाँच गर्नुहोस्।",
#             "कक्षा समय": "कक्षाहरू सामान्यतया बिहान ९ बजे देखि ४ बजे सम्म सञ्चालन हुन्छन्, तर तालिका कार्यक्रम र पाठ्यक्रमको आधारमा फरक हुन सक्छ।",
#             "भर्ना समय सीमा": "भर्नाको समय सीमा कार्यक्रम अनुसार फरक हुन्छ। कृपया हाम्रो वेबसाइट जाँच गर्नुहोस् वा तपाईंको रोजेको कार्यक्रमको लागि विशेष समय सीमाको लागि भर्ना कार्यालयमा सम्पर्क गर्नुहोस्।",
#             "यातायात विकल्पहरू": "धेरै यातायात विकल्पहरू छन् जसमा सार्वजनिक बसहरू, र गाडी चलाउने विद्यार्थीहरूको लागि पार्किङ सुविधाहरू समावेश छन्।",
#             "विदेश अध्ययन": "हो, हामीसँग अध्ययन विदेश कार्यक्रमहरू छन् जसले विद्यार्थीहरूलाई अन्तर्राष्ट्रिय अनुभव प्राप्त गर्न अनुमति दिन्छ। हामी पनि उत्साही विद्यार्थीहरूको लागि अन्तर्राष्ट्रिय यात्राको व्यवस्था गर्छौं।",
#             "आंशिक समयको काम": "हो, कलेजमा विद्यार्थीहरूका लागि आंशिक समयको कामका अवसरहरू उपलब्ध छन्। थप जानकारीको लागि कृपया हाम्रो क्यारियर सेवा कार्यालयमा जानुहोस्।",
#             "क्यान्टिन": "हामी विभिन्न प्रकारका भोजन विकल्पहरू सहित क्यान्टिन, कफी पसलहरू, र खाद्य अदालतहरू प्रदान गर्दछौं जुन विभिन्न आहार प्राथमिकताहरूलाई ध्यानमा राख्छ।",
#             "स्नातक आवश्यकताहरू": "स्नातक आवश्यकताहरू कार्यक्रम अनुसार फरक हुन्छन् तर सामान्यतया निर्दिष्ट संख्या क्रेडिटहरू पूरा गर्ने, आवश्यक पाठ्यक्रमहरू उत्तीर्ण गर्ने, र न्यूनतम GPA कायम गर्ने समावेश गर्दछ।",
#             "फिर्ता": "हाम्रो फिर्ता नीति कार्यक्रम र परिस्थितिहरू अनुसार फरक हुन्छ। शुल्क बुझाएको ७ दिन भित्र प्रवेश शुल्क फिर्ता हुनेछ तर शिक्षण शुल्क फिर्ता हुनेछैन।",
#             "विद्यार्थीको उपस्थिती": "नियमित उपस्थिती सबै विद्यार्थीहरूबाट अपेक्षित छ। उपस्थिती नीतिहरू सबै विद्यार्थीहरूको लागि ८०% भन्दा बढी अनिवार्य छ।",
#             "समाचार र घटनाहरू": "तपाईं हाम्रो आधिकारिक वेबसाइट र एपमा गइ, हाम्रो सामाजिक सञ्जाल च्यानलहरू पछ्याएर कलेज समाचार र घटनाहरूको बारेमा अद्यावधिक रहन सक्नुहुन्छ।",
#             "उद्योग पेशेवरहरू": "हामीले विद्यार्थीहरूलाई उद्योग नेताहरू र सम्भावित नियोक्ताहरूसँग जडान गर्न मद्दत गर्न अतिथि व्याख्यान, उद्योग प्यानलहरू, र नेटवर्किङ सत्रहरू जस्ता कार्यक्रमहरू आयोजना गर्छौं।",
#         }
#         self.tts_language = 'en'

#     def set_language(self, language_code):
#         self.tts_language = language_code if language_code in ['en', 'ne'] else 'en'

#     def ask_language_preference(self):
#         self.speak("Do you prefer to speak in English or Nepali?")
#         while True:
#             with sr.Microphone(sample_rate=16000) as source:
#                 self.recognizer.adjust_for_ambient_noise(source)
#                 audio = self.recognizer.listen(source, phrase_time_limit=5)
#             try:
#                 text = self.recognizer.recognize_google(audio, language='en').strip().lower()
#                 if "english" in text:
#                     self.set_language('en')
#                     self.speak("You have selected English. How can I assist you?")
#                     break
#                 elif "nepali" in text or "नेपाली" in text:
#                     self.set_language('ne')
#                     self.speak("तपाईंले नेपाली रोज्नु भएको छ। म तपाईंलाई कसरी मद्दत गर्न सक्छु?")
#                     break
#                 else:
#                     self.speak("Sorry, I didn't understand. Please say English or Nepali.")
#             except sr.UnknownValueError:
#                 self.speak("Sorry, I couldn't understand. Please say English or Nepali.")
#             except sr.RequestError as e:
#                 self.speak(f"Error: {e}")

#     def start_transcription(self):
#         welcome_message = "Welcome! How can I help you today?" if self.tts_language == 'en' else "स्वागत छ! म तपाईंलाई आज कसरी मद्दत गर्न सक्छु?"
#         self.speak(welcome_message)
#         while True:
#             with sr.Microphone(sample_rate=16000) as source:
#                 self.recognizer.adjust_for_ambient_noise(source)
#                 audio = self.recognizer.listen(source, phrase_time_limit=5)
#             try:
#                 text = self.recognizer.recognize_google(audio, language='ne-IN' if self.tts_language == 'ne' else 'en-US').strip()
#                 self.full_transcript.append({"role": "user", "content": text})

#                 # Check if there is a predefined response
#                 response_text = self.check_predefined_qa(text)
#                 if response_text:
#                     self.full_transcript.append({"role": "assistant", "content": response_text})
#                     self.speak(response_text)
#                 else:
#                     # Generate AI response if no predefined response
#                     ai_response = self.generate_ai_response(text)
#                     self.full_transcript.append({"role": "assistant", "content": ai_response})
#                     self.speak(ai_response)

#                 if "thank you" in text.lower() or "धन्यवाद" in text:
#                     exit_message = "Goodbye! If you have any more questions, feel free to ask." if self.tts_language == 'en' else "अलविदा! यदि तपाईंसँग अरु प्रश्नहरू छन् भने, कृपया सोध्नुहोस्।"
#                     self.speak(exit_message)
#                     break
#             except sr.UnknownValueError:
#                 self.speak("Sorry, couldn't understand.")
#             except sr.RequestError as e:
#                 self.speak(f"Error: {e}")

#     def check_predefined_qa(self, text):
#         normalized_text = text.lower()
#         return self.predefined_qa.get(normalized_text, None)

#     def generate_ai_response(self, text):
#         try:
#             response = self.chat.send_message(text, stream=True)
#             ai_response = "".join(chunk.text for chunk in response)
#             if not ai_response:
#                 print("No response text received.")
#                 return "Sorry, I couldn't generate a response."
#             first_sentence = ai_response.split(". ")[0].strip()
#             print(f"Generated AI Response: {first_sentence}")
#             return first_sentence
#         except Exception as e:
#             print(f"Error processing AI response: {e}")
#             return "Sorry, I couldn't generate a response."

#     def speak(self, text):
#         if not text or text.strip() == "":
#             print("No text provided to speak.")
#             return

#         try:
#             print(f"TTS Text: {text}")  # Debugging line
#             tts = gTTS(text=text, lang=self.tts_language)
#             fp = io.BytesIO()
#             tts.write_to_fp(fp)
#             fp.seek(0)
#             pygame.mixer.music.load(fp)
#             pygame.mixer.music.play()
#             while pygame.mixer.music.get_busy():
#                 pygame.time.Clock().tick(10)
#         except Exception as e:
#             print(f"Error in TTS: {e}")

# # Instantiate AI Assistant
# assistant = AI_Assistant()

# # Flask Routes
# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/recognize', methods=['POST'])
# def recognize():
#     try:
#         data = request.json
#         language = data.get('language', 'en')
#         assistant.set_language(language)
#         assistant.ask_language_preference()
#         assistant.start_transcription()
#         return jsonify({"status": "started"})
#     except Exception as e:
#         print("Error:", str(e))
#         return jsonify({"error": str(e)}), 400

# @app.route('/generate', methods=['POST'])
# def generate():
#     try:
#         data = request.json
#         text = data['text']
#         response = assistant.generate_ai_response(text)
#         return jsonify({"response": response})
#     except Exception as e:
#         print("Error:", str(e))
#         return jsonify({"error": str(e)}), 400

# @app.route('/speak', methods=['POST'])
# def speak():
#     try:
#         data = request.json
#         text = data['text']
#         assistant.speak(text)
#         return jsonify({"status": "spoken"})
#     except Exception as e:
#         print("Error:", str(e))
#         return jsonify({"error": str(e)}), 400

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, request, jsonify
# import speech_recognition as sr
# import google.generativeai as genai
# import pygame
# from gtts import gTTS
# import io
# import os

# app = Flask(__name__)

# class AI_Assistant:
#     def __init__(self):
#         genai.configure(api_key='AIzaSyAIGpQ_3eawfsmYoBi-RPpq6H3Dohp5Eco')  # Replace with your actual API key
#         self.model = genai.GenerativeModel("gemini-pro")
#         self.chat = self.model.start_chat(history=[])
#         self.recognizer = sr.Recognizer()
#         self.full_transcript = []
#         pygame.mixer.init()
#         self.predefined_qa = {
#             "what is your name": "My name is Jack, your virtual assistant.",
#             "how are you feeling today": "I am just a bunch of code, but I am here to help!",
#             "requirement process": "Generally, students need to have completed their higher secondary education (10+2) or equivalent with a minimum specified percentage. Specific programs may have additional requirements, such as a background in science for IT or engineering courses.",
#             "admission process": "Completed application form Academic transcripts and certificates Passport-sized photographs Identification proof (citizenship or passport) Entrance exam scorecard",
#             "entrance": "Yes, Softwarica College often requires an entrance exam for admission, particularly for competitive programs. The format typically includes multiple-choice questions covering subjects relevant to the chosen program.",
#             "fee": "The fee structure varies by program. Detailed fee information is usually provided on the college’s official website or can be obtained from the admissions office.",
#             "scholarship": "Scholarships based on merit and need are available. Scholarships are often awarded to students with excellent academic performance or those in financial need.",
#             "ratio": "This ratio can vary but is generally designed to ensure personalized attention and support for students.",
#             "class": "We typically have moderate class sizes, allowing for interactive learning environments.",
#             "intern": "Opportunities for research and internships are available, often facilitated through partnerships with industries and organizations.",
#             "library": "The college provides a well-stocked library with academic books, journals, and digital resources.",
#             "lab": "Equipped with the latest technology and software to support IT and engineering students.",
#             "sport": "Facilities for various sports, including basketball, football, and indoor games, are available.",
#             "canteen": "We provide the best quality of food services which is affordable.",
#             "club": "Various student clubs and societies for cultural, academic, and recreational activities.",
#             "event": "Regular events, including festivals, sports meets, and competitions, are organized.",
#             "volunteer": "You can participate in different events and be a volunteer.",
#             "leader": "Students can participate in leadership roles within clubs, student councils, and other organizations.",
#             "career": "Career counseling, job placement support, and workshops are provided to assist students in career planning.",
#             "tour": "Organized to provide practical exposure and experiential learning.",
#             "job fairs": "Yes, we organize job fairs each semester where students can meet potential employers and learn about job opportunities.",
#             "address": "Softwarica College of IT is located at Dillibazar, Kathmandu.",
#             "courses": "We have courses of BSc (Hons) Computing, BSc (Hons) Ethical Hacking and Cybersecurity, BSc (Hons) Computer Science with Artificial Intelligence",
#             "enroll now": "That's great! Which course would you like to enroll in?",
#             "faculty": "Both faculty from Science and Management can admit in this college and proceed with their study in IT.",
#             "apply?": "You can apply online through our official website or visit our admissions office for assistance with the application process.",
#             "documents": "You will need to submit a completed application form, academic transcripts and certificates, passport-sized photographs, and identification proof.",
#             "semester start": "The semester typically starts in September. For exact dates, please check our academic calendar on the official website and app.",
#             "class timings": "Classes are typically held from 9 AM to 4 PM, but the schedule may vary depending on the program and course.",
#             "admission deadline": "The admission deadlines vary by program. Please check our website or contact the admissions office for the specific deadlines for your chosen program.",
#             "transportation options": "There are several transportation options including public buses, and parking facilities for students who drive.",
#             "abroad study ": "Yes, we have study abroad programs that allow students to gain international experience. We also provide international trip for enthusiastic students.",
#             "part-time job": "Yes, there are part-time job opportunities available on campus for students. Please visit our career services office for more information.",
#             "canteen": "We offer a variety of dining options including canteen, coffee shops, and food courts that cater to different dietary preferences.",
#             "graduation requirements": "Graduation requirements vary by program but generally include completing a specified number of credits, passing required courses, and maintaining a minimum GPA.",
#              " refund": "Our refund policy varies by program and circumstance. Admission fees will be refunded with decrease  20% but not the tuition fees",
#             "student attendance": "Regular attendance is expected from all students. Attendance policies is that every student should have above 80% mandatory.",
#             "news and events?": "You can stay updated with college news and events by visiting our official app and  website, following our social media channels.",
#             "industry professionals": "We organize events such as guest lectures, industry panels, and networking sessions with professionals to help students connect with industry leaders and potential employers.",
#             # Add other predefined Q&A pairs here
#             "तपाई कस्तो हुनुहुन्छ": "म कोडको एउटा गुच्छा मात्र हुँ, तर म तपाईलाई मद्दत गर्न यहाँ छु!",
#             # Add other Nepali Q&A pairs here
#         }
#         self.tts_language = 'en'

#     def set_language(self, language_code):
#         self.tts_language = language_code if language_code in ['en', 'ne'] else 'en'

#     def ask_language_preference(self):
#         self.speak("Do you prefer to speak in English or Nepali?")
#         while True:
#             with sr.Microphone(sample_rate=16000) as source:
#                 self.recognizer.adjust_for_ambient_noise(source)
#                 audio = self.recognizer.listen(source, phrase_time_limit=5)
#             try:
#                 text = self.recognizer.recognize_google(audio, language='en').strip().lower()
#                 if "english" in text:
#                     self.set_language('en')
#                     self.speak("You have selected English. How can I assist you?")
#                     break
#                 elif "nepali" in text or "नेपाली" in text:
#                     self.set_language('ne')
#                     self.speak("तपाईंले नेपाली रोज्नु भएको छ। म तपाईंलाई कसरी मद्दत गर्न सक्छु?")
#                     break
#                 else:
#                     self.speak("Sorry, I didn't understand. Please say English or Nepali.")
#             except sr.UnknownValueError:
#                 self.speak("Sorry, I couldn't understand. Please say English or Nepali.")
#             except sr.RequestError as e:
#                 self.speak(f"Error: {e}")

#     def start_transcription(self):
#         welcome_message = "Welcome! How can I help you today?" if self.tts_language == 'en' else "स्वागत छ! म तपाईंलाई आज कसरी मद्दत गर्न सक्छु?"
#         self.speak(welcome_message)
#         while True:
#             with sr.Microphone(sample_rate=16000) as source:
#                 self.recognizer.adjust_for_ambient_noise(source)
#                 audio = self.recognizer.listen(source, phrase_time_limit=5)
#             try:
#                 text = self.recognizer.recognize_google(audio, language='ne-IN' if self.tts_language == 'ne' else 'en-US').strip()
#                 self.full_transcript.append({"role": "user", "content": text})

#                 # Check if there is a predefined response
#                 response_text = self.check_predefined_qa(text)
#                 if response_text:
#                     self.full_transcript.append({"role": "assistant", "content": response_text})
#                     self.speak(response_text)
#                 else:
#                     # Generate AI response if no predefined response
#                     ai_response = self.generate_ai_response(text)
#                     self.full_transcript.append({"role": "assistant", "content": ai_response})
#                     self.speak(ai_response)

#                 if "thank you" in text.lower() or "धन्यवाद" in text:
#                     exit_message = "Goodbye! If you have any more questions, feel free to ask." if self.tts_language == 'en' else "अलविदा! यदि तपाईंसँग अरु प्रश्नहरू छन् भने, कृपया सोध्नुहोस्।"
#                     self.speak(exit_message)
#                     break
#             except sr.UnknownValueError:
#                 self.speak("Sorry, couldn't understand.")
#             except sr.RequestError as e:
#                 self.speak(f"Error: {e}")

#     def check_predefined_qa(self, text):
#         normalized_text = text.lower()
#         return self.predefined_qa.get(normalized_text, None)

#     def generate_ai_response(self, text):
#         try:
#             response = self.chat.send_message(text, stream=True)
#             ai_response = "".join(chunk.text for chunk in response)
#             if not ai_response:
#                 print("No response text received.")
#                 return "Sorry, I couldn't generate a response."
#             first_sentence = ai_response.split(". ")[0].strip()
#             print(f"Generated AI Response: {first_sentence}")
#             return first_sentence
#         except Exception as e:
#             print(f"Error processing AI response: {e}")
#             return "Sorry, I couldn't generate a response."

#     def speak(self, text):
#         if not text or text.strip() == "":
#             print("No text provided to speak.")
#             return

#         try:
#             print(f"TTS Text: {text}")  # Debugging line
#             tts = gTTS(text=text, lang=self.tts_language)
#             fp = io.BytesIO()
#             tts.write_to_fp(fp)
#             fp.seek(0)
#             pygame.mixer.music.load(fp)
#             pygame.mixer.music.play()
#             while pygame.mixer.music.get_busy():
#                 pygame.time.Clock().tick(10)
#         except Exception as e:
#             print(f"Error in TTS: {e}")

# # Instantiate AI Assistant
# assistant = AI_Assistant()

# # Flask Routes
# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/recognize', methods=['POST'])
# def recognize():
#     try:
#         data = request.json
#         language = data.get('language', 'en')
#         assistant.set_language(language)
#         assistant.ask_language_preference()
#         assistant.start_transcription()
#         return jsonify({"status": "started"})
#     except Exception as e:
#         print("Error:", str(e))
#         return jsonify({"error": str(e)}), 400

# @app.route('/generate', methods=['POST'])
# def generate():
#     try:
#         data = request.json
#         text = data['text']
#         response = assistant.generate_ai_response(text)
#         return jsonify({"response": response})
#     except Exception as e:
#         print("Error:", str(e))
#         return jsonify({"error": str(e)}), 400

# @app.route('/speak', methods=['POST'])
# def speak():
#     try:
#         data = request.json
#         text = data['text']
#         assistant.speak(text)
#         return jsonify({"status": "spoken"})
#     except Exception as e:
#         print("Error:", str(e))
#         return jsonify({"error": str(e)}), 400

# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, render_template, request, jsonify
# import speech_recognition as sr
# import google.generativeai as genai
# import pygame
# from gtts import gTTS
# import io
# import os

# app = Flask(__name__)

# class AI_Assistant:
#     def __init__(self):
#         genai.configure(api_key='AIzaSyAIGpQ_3eawfsmYoBi-RPpq6H3Dohp5Eco')  # Replace with your actual API key
#         self.model = genai.GenerativeModel("gemini-pro")
#         self.chat = self.model.start_chat(history=[])
#         self.recognizer = sr.Recognizer()
#         self.full_transcript = []
#         pygame.mixer.init()
#         self.predefined_qa = {
#             "what is your name": "My name is Jack, your virtual assistant.",
#             "how are you feeling today": "I am just a bunch of code, but I am here to help!",
#             "requirement process": "Generally, students need to have completed their higher secondary education (10+2) or equivalent with a minimum specified percentage. Specific programs may have additional requirements, such as a background in science for IT or engineering courses.",
#             "admission process": "Completed application form Academic transcripts and certificates Passport-sized photographs Identification proof (citizenship or passport) Entrance exam scorecard",
#             "entrance": "Yes, Softwarica College often requires an entrance exam for admission, particularly for competitive programs. The format typically includes multiple-choice questions covering subjects relevant to the chosen program.",
#             "fee": "The fee structure varies by program. Detailed fee information is usually provided on the college’s official website or can be obtained from the admissions office.",
#             "scholarship": "Scholarships based on merit and need are available. Scholarships are often awarded to students with excellent academic performance or those in financial need.",
#             "ratio": "This ratio can vary but is generally designed to ensure personalized attention and support for students.",
#             "class": "We typically have moderate class sizes, allowing for interactive learning environments.",
#             "intern": "Opportunities for research and internships are available, often facilitated through partnerships with industries and organizations.",
#             "library": "The college provides a well-stocked library with academic books, journals, and digital resources.",
#             "lab": "Equipped with the latest technology and software to support IT and engineering students.",
#             "sport": "Facilities for various sports, including basketball, football, and indoor games, are available.",
#             "canteen": "We provide the best quality of food services which is affordable.",
#             "club": "Various student clubs and societies for cultural, academic, and recreational activities.",
#             "event": "Regular events, including festivals, sports meets, and competitions, are organized.",
#             "volunteer": "You can participate in different events and be a volunteer.",
#             "leader": "Students can participate in leadership roles within clubs, student councils, and other organizations.",
#             "career": "Career counseling, job placement support, and workshops are provided to assist students in career planning.",
#             "tour": "Organized to provide practical exposure and experiential learning.",
#             "job fairs": "Yes, we organize job fairs each semester where students can meet potential employers and learn about job opportunities.",
#             "address": "Softwarica College of IT is located at Dillibazar, Kathmandu.",
#             "courses": "We have courses of BSc (Hons) Computing, BSc (Hons) Ethical Hacking and Cybersecurity, BSc (Hons) Computer Science with Artificial Intelligence",
#             "enroll now": "That's great! Which course would you like to enroll in?",
#             "faculty": "Both faculty from Science and Management can admit in this college and proceed with their study in IT.",
#             "apply?": "You can apply online through our official website or visit our admissions office for assistance with the application process.",
#             "documents": "You will need to submit a completed application form, academic transcripts and certificates, passport-sized photographs, and identification proof.",
#             "semester start": "The semester typically starts in September. For exact dates, please check our academic calendar on the official website and app.",
#             "class timings": "Classes are typically held from 9 AM to 4 PM, but the schedule may vary depending on the program and course.",
#             "admission deadline": "The admission deadlines vary by program. Please check our website or contact the admissions office for the specific deadlines for your chosen program.",
#             "transportation options": "There are several transportation options including public buses, and parking facilities for students who drive.",
#             "abroad study ": "Yes, we have study abroad programs that allow students to gain international experience. We also provide international trip for enthusiastic students.",
#             "part-time job": "Yes, there are part-time job opportunities available on campus for students. Please visit our career services office for more information.",
#             "canteen": "We offer a variety of dining options including canteen, coffee shops, and food courts that cater to different dietary preferences.",
#             "graduation requirements": "Graduation requirements vary by program but generally include completing a specified number of credits, passing required courses, and maintaining a minimum GPA.",
#              " refund": "Our refund policy varies by program and circumstance. Admission fees will be refunded with decrease  20% but not the tuition fees",
#             "student attendance": "Regular attendance is expected from all students. Attendance policies is that every student should have above 80% mandatory.",
#             "news and events?": "You can stay updated with college news and events by visiting our official app and  website, following our social media channels.",
#             "industry professionals": "We organize events such as guest lectures, industry panels, and networking sessions with professionals to help students connect with industry leaders and potential employers.",
#             # Add other predefined Q&A pairs here
#             "तपाई कस्तो हुनुहुन्छ": "म कोडको एउटा गुच्छा मात्र हुँ, तर म तपाईलाई मद्दत गर्न यहाँ छु!",
#             # Add other Nepali Q&A pairs here
#         }
#         self.tts_language = 'en'

#     def set_language(self, language_code):
#         self.tts_language = language_code if language_code in ['en', 'ne'] else 'en'

#     def ask_language_preference(self):
#         self.speak("Do you prefer to speak in English or Nepali?")
#         while True:
#             with sr.Microphone(sample_rate=16000) as source:
#                 self.recognizer.adjust_for_ambient_noise(source)
#                 audio = self.recognizer.listen(source, phrase_time_limit=5)
#             try:
#                 text = self.recognizer.recognize_google(audio, language='en').strip().lower()
#                 if "english" in text:
#                     self.set_language('en')
#                     self.speak("You have selected English. How can I assist you?")
#                     break
#                 elif "nepali" in text or "नेपाली" in text:
#                     self.set_language('ne')
#                     self.speak("तपाईंले नेपाली रोज्नु भएको छ। म तपाईंलाई कसरी मद्दत गर्न सक्छु?")
#                     break
#                 else:
#                     self.speak("Sorry, I didn't understand. Please say English or Nepali.")
#             except sr.UnknownValueError:
#                 self.speak("Sorry, I couldn't understand. Please say English or Nepali.")
#             except sr.RequestError as e:
#                 self.speak(f"Error: {e}")

#     def start_transcription(self):
#         welcome_message = "Welcome! How can I help you today?" if self.tts_language == 'en' else "स्वागत छ! म तपाईंलाई आज कसरी मद्दत गर्न सक्छु?"
#         self.speak(welcome_message)
#         while True:
#             with sr.Microphone(sample_rate=16000) as source:
#                 self.recognizer.adjust_for_ambient_noise(source)
#                 audio = self.recognizer.listen(source, phrase_time_limit=5)
#             try:
#                 text = self.recognizer.recognize_google(audio, language='ne-IN' if self.tts_language == 'ne' else 'en-US').strip()
#                 self.full_transcript.append({"role": "user", "content": text})

#                 # Check if there is a predefined response
#                 response_text = self.check_predefined_qa(text)
#                 if response_text:
#                     self.full_transcript.append({"role": "assistant", "content": response_text})
#                     self.speak(response_text)
#                 else:
#                     # Generate AI response if no predefined response
#                     ai_response = self.generate_ai_response(text)
#                     self.full_transcript.append({"role": "assistant", "content": ai_response})
#                     self.speak(ai_response)

#                 if "thank you" in text.lower() or "धन्यवाद" in text:
#                     exit_message = "Goodbye! If you have any more questions, feel free to ask." if self.tts_language == 'en' else "अलविदा! यदि तपाईंसँग अरु प्रश्नहरू छन् भने, कृपया सोध्नुहोस्।"
#                     self.speak(exit_message)
#                     break
#             except sr.UnknownValueError:
#                 self.speak("Sorry, couldn't understand.")
#             except sr.RequestError as e:
#                 self.speak(f"Error: {e}")

#     def check_predefined_qa(self, text):
#         normalized_text = text.lower()
#         for keyword, response in self.predefined_qa.items():
#             if keyword in normalized_text:
#                 return response
#         return None

#     def generate_ai_response(self, text):
#         try:
#             response = self.chat.send_message(text, stream=True)
#             ai_response = "".join(chunk.text for chunk in response)
#             if not ai_response:
#                 print("No response text received.")
#                 return "Sorry, I couldn't generate a response."
#             first_sentence = ai_response.split(". ")[0].strip()
#             print(f"Generated AI Response: {first_sentence}")
#             return first_sentence
#         except Exception as e:
#             print(f"Error processing AI response: {e}")
#             return "Sorry, I couldn't generate a response."

#     def speak(self, text):
#         if not text or text.strip() == "":
#             print("No text provided to speak.")
#             return

#         try:
#             print(f"TTS Text: {text}")  # Debugging line
#             tts = gTTS(text=text, lang=self.tts_language)
#             fp = io.BytesIO()
#             tts.write_to_fp(fp)
#             fp.seek(0)
#             pygame.mixer.music.load(fp)
#             pygame.mixer.music.play()
#             while pygame.mixer.music.get_busy():
#                 pygame.time.Clock().tick(10)
#         except Exception as e:
#             print(f"Error in TTS: {e}")

# # Instantiate AI Assistant
# assistant = AI_Assistant()

# # Flask Routes
# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/recognize', methods=['POST'])
# def recognize():
#     try:
#         data = request.json
#         language = data.get('language', 'en')
#         assistant.set_language(language)
#         assistant.ask_language_preference()
#         assistant.start_transcription()
#         return jsonify({"status": "started"})
#     except Exception as e:
#         print("Error:", str(e))
#         return jsonify({"error": str(e)}), 400

# @app.route('/generate', methods=['POST'])
# def generate():
#     try:
#         data = request.json
#         text = data['text']
#         response = assistant.generate_ai_response(text)
#         return jsonify({"response": response})
#     except Exception as e:
#         print("Error:", str(e))
#         return jsonify({"error": str(e)}), 400

# @app.route('/speak', methods=['POST'])
# def speak():
#     try:
#         data = request.json
#         text = data['text']
#         assistant.speak(text)
#         return jsonify({"status": "spoken"})
#     except Exception as e:
#         print("Error:", str(e))
#         return jsonify({"error": str(e)}), 400

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import google.generativeai as genai
import pygame
from gtts import gTTS
import io
import os
import cv2  # Import OpenCV

app = Flask(__name__)

class AI_Assistant:
    def __init__(self):
        genai.configure(api_key='AIzaSyBQLWLmiczPrGCKtikCOI8d1dmpvTk-vdA')  # Replace with your actual API key
        self.model = genai.GenerativeModel("gemini-pro")
        self.chat = self.model.start_chat(history=[])
        self.recognizer = sr.Recognizer()
        self.full_transcript = []
        pygame.mixer.init()
        self.predefined_qa = {
            "what is your name": "My name is Jack, your virtual assistant.",
            "how are you feeling today": "I am just a bunch of code, but I am here to help!",
            "requirement process": "Generally, students need to have completed their higher secondary education (10+2) or equivalent with a minimum specified percentage. Specific programs may have additional requirements, such as a background in science for IT or engineering courses.",
            "admission process": "Completed application form Academic transcripts and certificates Passport-sized photographs Identification proof (citizenship or passport) Entrance exam scorecard",
            "entrance": "Yes, Softwarica College often requires an entrance exam for admission, particularly for competitive programs. The format typically includes multiple-choice questions covering subjects relevant to the chosen program.",
            "fee": "The fee structure varies by program. Detailed fee information is usually provided on the college’s official website or can be obtained from the admissions office.",
            "scholarship": "Scholarships based on merit and need are available. Scholarships are often awarded to students with excellent academic performance or those in financial need.",
            "ratio": "This ratio can vary but is generally designed to ensure personalized attention and support for students.",
            "class": "We typically have moderate class sizes, allowing for interactive learning environments.",
            "intern": "Opportunities for research and internships are available, often facilitated through partnerships with industries and organizations.",
            "library": "The college provides a well-stocked library with academic books, journals, and digital resources.",
            "lab": "Equipped with the latest technology and software to support IT and engineering students.",
            "sport": "Facilities for various sports, including basketball, football, and indoor games, are available.",
            "canteen": "We provide the best quality of food services which is affordable.",
            "club": "Various student clubs and societies for cultural, academic, and recreational activities.",
            "event": "Regular events, including festivals, sports meets, and competitions, are organized.",
            "volunteer": "You can participate in different events and be a volunteer.",
            "leader": "Students can participate in leadership roles within clubs, student councils, and other organizations.",
            "career": "Career counseling, job placement support, and workshops are provided to assist students in career planning.",
            "tour": "Organized to provide practical exposure and experiential learning.",
            "job ": "Yes, we organize job fairs each semester where students can meet potential employers and learn about job opportunities.",
            "address": "Softwarica College of IT is located at Dillibazar, Kathmandu.",
            "courses": "We have courses of BSc (Hons) Computing, BSc (Hons) Ethical Hacking and Cybersecurity, BSc (Hons) Computer Science with Artificial Intelligence",
            "enroll ": "That's great! Which course would you like to enroll in?",
            "faculty": "Both faculty from Science and Management can admit in this college and proceed with their study in IT.",
            "apply?": "You can apply online through our official website or visit our admissions office for assistance with the application process.",
            "documents": "You will need to submit a completed application form, academic transcripts and certificates, passport-sized photographs, and identification proof.",
            "semester start": "The semester typically starts in September. For exact dates, please check our academic calendar on the official website and app.",
            "timings": "Classes are typically held from 9 AM to 4 PM, but the schedule may vary depending on the program and course.",
            "admission deadline": "The admission deadlines vary by program. Please check our website or contact the admissions office for the specific deadlines for your chosen program.",
            "transportation options": "There are several transportation options including public buses, and parking facilities for students who drive.",
            "abroad study ": "Yes, we have study abroad programs that allow students to gain international experience. We also provide international trip for enthusiastic students.",
            "part-time job": "Yes, there are part-time job opportunities available on campus for students. Please visit our career services office for more information.",
            "canteen": "We offer a variety of dining options including canteen, coffee shops, and food courts that cater to different dietary preferences.",
            "graduation": "Graduation requirements vary by program but generally include completing a specified number of credits, passing required courses, and maintaining a minimum GPA.",
             "refund": "Our refund policy varies by program and circumstance. Admission fees will be refunded with decrease  20% but not the tuition fees",
            "attendance": "Regular attendance is expected from all students. Attendance policies is that every student should have above 80% mandatory.",
            "news and events?": "You can stay updated with college news and events by visiting our official app and  website, following our social media channels.",
            "industry professionals": "We organize events such as guest lectures, industry panels, and networking sessions with professionals to help students connect with industry leaders and potential employers.",
            # ... (rest of the predefined Q&A)
            "तपाई कस्तो हुनुहुन्छ": "म कोडको एउटा गुच्छा मात्र हुँ, तर म तपाईलाई मद्दत गर्न यहाँ छु!",
            "निवेदन गर्नु": "तपाईं हाम्रो आधिकारिक वेबसाइट मार्फत अनलाइन आवेदन दिन सक्नुहुन्छ वा आवेदन प्रक्रियामा सहयोगको लागि हाम्रो भर्ना कार्यालयमा जान सक्नुहुन्छ।",
            "कागजातहरू": "तपाईंले पूरा भएको आवेदन फारम, शैक्षिक प्रतिलिपिहरू र प्रमाणपत्रहरू, राहदानी आकारका फोटोहरू, र पहिचान प्रमाण पेश गर्नुपर्नेछ।",
            "सेमेस्टर सुरुt": "सेमेस्टर सामान्यतया सेप्टेम्बरमा सुरु हुन्छ। ठ्याक्कै मितिहरूको लागि, कृपया हाम्रो आधिकारिक वेबसाइट र एपमा हाम्रो शैक्षिक पात्रो जाँच गर्नुहोस्।",
            "  कक्षा समय": "कक्षाहरू सामान्यतया बिहान ९ बजेदेखि अपराह्न ४ बजेसम्म सञ्चालन हुन्छन्, तर कार्यक्रम र पाठ्यक्रमको आधारमा तालिका फरक हुन सक्छ।",
            "भर्ना समय सीमा": "प्रवेशको अन्तिम मिति कार्यक्रम अनुसार फरक हुन्छ। कृपया हाम्रो वेबसाइट जाँच गर्नुहोस् वा तपाईंको रोजेको कार्यक्रमको लागि विशेष मितिहरूको लागि भर्ना कार्यालयमा सम्पर्क गर्नुहोस्।",
            "यातायात विकल्प": "क्याम्पस सम्म पुग्न सार्वजनिक बसहरू, र विद्यार्थीहरूले सवारी चलाउनको लागि पार्किङ सुविधा जस्ता धेरै यातायात विकल्पहरू उपलब्ध छन्।",
            "विदेश अध्ययन": "हो, हामीसँग अन्तर्राष्ट्रिय अनुभव प्राप्त गर्न विद्यार्थीहरूलाई अनुमति दिने अध्ययन विदेश कार्यक्रमहरू छन्। हामी उत्साही विद्यार्थीहरूको लागि अन्तर्राष्ट्रिय यात्राको पनि व्यवस्था गर्छौं।",
            "part-time job": "हो, क्याम्पसमा विद्यार्थीहरूको लागि आंशिक समयको कामका अवसरहरू उपलब्ध छन्। थप जानकारीको लागि कृपया हाम्रो क्यारियर सेवाहरू कार्यालयमा जानुहोस्।",
            "क्यान्टीन": "हामी विभिन्न आहार प्राथमिकताहरूलाई पूरा गर्ने क्यान्टीन, कफी पसलहरू, र फूड कोर्ट सहितको भोजन विकल्पहरूको विविधता प्रस्ताव गर्दछौं।",
            "स्नातक आवश्यकताहरू": "स्नातक आवश्यकताहरू कार्यक्रम अनुसार फरक हुन्छन् तर सामान्यतया निर्दिष्ट संख्या क्रेडिटहरू पूरा गर्न, आवश्यक पाठ्यक्रमहरू पास गर्न, र न्यूनतम जीपीए कायम राख्न समावेश गर्दछ।",
            "फिर्ता": "हाम्रो फिर्ता नीति कार्यक्रम र परिस्थिति अनुसार फरक हुन्छ। भर्ना शुल्क २०% घटाएर फिर्ता गरिनेछ तर ट्यूसन शुल्क फिर्ता गरिने छैन।",
            "विद्यार्थी उपस्थिति": "सबै विद्यार्थीहरूबाट नियमित उपस्थितिको अपेक्षा गरिन्छ। उपस्थिति नीतिहरू अनुसार प्रत्येक विद्यार्थीको उपस्थिति ८०% भन्दा माथि अनिवार्य हुनुपर्छ।",
            "समाचार र घटनाहरू" :"तपाईं हाम्रो आधिकारिक एप र वेबसाइट भ्रमण गरेर, हाम्रो सामाजिक मिडिया च्यानलहरू अनुसरण गरेर कलेज समाचार र घटनाहरू अपडेट गर्न सक्नुहुन्छ।",
            "उद्योग पेशेवरहरू": "हामी अतिथि व्याख्यानहरू, उद्योग प्यानलहरू, र उद्योग नेताहरू र सम्भावित नियोक्ताहरूको साथ विद्यार्थीहरूलाई जडान गर्न मद्दत गर्न पेशेवरहरूका साथ नेटवर्किङ सत्रहरू जस्ता कार्यक्रमहरूको आयोजन गर्छौं।"
            # Add other Nepali Q&A pairs here
        }
        self.tts_language = 'en'

    def set_language(self, language_code):
        self.tts_language = language_code if language_code in ['en', 'ne'] else 'en'

    def ask_language_preference(self):
        self.speak("Do you prefer to speak in English or Nepali?")
        while True:
            with sr.Microphone(sample_rate=16000) as source:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source, phrase_time_limit=10)
            try:
                text = self.recognizer.recognize_google(audio, language='en').strip().lower()
                if "english" in text:
                    self.set_language('en')
                    self.speak("You have selected English. How can I assist you?")
                    break
                elif "nepali" in text or "नेपाली" in text:
                    self.set_language('ne')
                    self.speak("तपाईंले नेपाली रोज्नु भएको छ। म तपाईंलाई कसरी मद्दत गर्न सक्छु?")
                    break
                else:
                    self.speak("Sorry, I didn't understand. Please say English or Nepali.")
            except sr.UnknownValueError:
                self.speak("Sorry, I couldn't understand. Please say English or Nepali.")
            except sr.RequestError as e:
                self.speak(f"Error: {e}")

    def start_transcription(self):
        welcome_message = "Welcome! How can I help you today?" if self.tts_language == 'en' else "स्वागत छ! म तपाईंलाई आज कसरी मद्दत गर्न सक्छु?"
        self.speak(welcome_message)
        while True:
            with sr.Microphone(sample_rate=16000) as source:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source, phrase_time_limit=5)
            try:
                text = self.recognizer.recognize_google(audio, language='ne-IN' if self.tts_language == 'ne' else 'en-US').strip()
                self.full_transcript.append({"role": "user", "content": text})
                print(f"Human asked: {text}")  

                # Check if there is a predefined response
                response_text = self.check_predefined_qa(text)
                if response_text:
                    self.full_transcript.append({"role": "assistant", "content": response_text})
                    self.speak(response_text)
                else:
                    # Generate AI response if no predefined response
                    ai_response = self.generate_ai_response(text)
                    self.full_transcript.append({"role": "assistant", "content": ai_response})
                    self.speak(ai_response)

                if "thank you" in text.lower() or "धन्यवाद" in text:
                    exit_message = "Goodbye! If you have any more questions, feel free to ask." if self.tts_language == 'en' else "अलविदा! यदि तपाईंसँग अरु प्रश्नहरू छन् भने, कृपया सोध्नुहोस्।"
                    self.speak(exit_message)
                    break
            except sr.UnknownValueError:
                self.speak("Sorry, couldn't understand.")
            except sr.RequestError as e:
                self.speak(f"Error: {e}")

    def check_predefined_qa(self, text):
        normalized_text = text.lower()
        for keyword, response in self.predefined_qa.items():
            if keyword in normalized_text:
                return response
        return None

    def generate_ai_response(self, text):
        try:
            response = self.chat.send_message(text, stream=True)
            ai_response = "".join(chunk.text for chunk in response)
            if not ai_response:
                print("No response text received.")
                return "Sorry, I couldn't generate a response."
            first_sentence = ai_response.split(". ")[0].strip()
            print(f"Generated AI Response: {first_sentence}")
            return first_sentence
        except Exception as e:
            print(f"Error processing AI response: {e}")
            return "Sorry, I couldn't generate a response."

    def speak(self, text):
        if not text or text.strip() == "":
            print("No text provided to speak.")
            return

        try:
            print(f"TTS Text: {text}")  # Debugging line
            tts = gTTS(text=text, lang=self.tts_language)
            fp = io.BytesIO()
            tts.write_to_fp(fp)
            fp.seek(0)
            pygame.mixer.music.load(fp)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        except Exception as e:
            print(f"Error in TTS: {e}")

# Instantiate AI Assistant
assistant = AI_Assistant()

def detect_face():
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cap.release()
            cv2.destroyAllWindows()
            return True  # Face detected

        cv2.imshow('Face Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return False

# Flask Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recognize', methods=['POST'])
def recognize():
    if detect_face():
        try:
            data = request.json
            language = data.get('language', 'en')
            assistant.set_language(language)
            assistant.ask_language_preference()
            assistant.start_transcription()
            return jsonify({"status": "started"})
        except Exception as e:
            print("Error:", str(e))
            return jsonify({"error": str(e)}), 400
    else:
        return jsonify({"error": "No face detected"}), 400

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        text = data['text']
        response = assistant.generate_ai_response(text)
        return jsonify({"response": response})
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)}), 400

@app.route('/speak', methods=['POST'])
def speak():
    try:
        data = request.json
        text = data['text']
        assistant.speak(text)
        return jsonify({"status": "spoken"})
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)




