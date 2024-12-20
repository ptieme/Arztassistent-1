from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Page d'accueil avec un message de bienvenue

@app.route('/conversation', methods=['POST', 'GET'])
def conversation():
    if request.method == 'POST':
        user_message = request.form['message']
        
        # Logique de réponse du serveur
        if "krank" in user_message.lower():
            response = "Was haben Sie?"
        elif "grippe" in user_message.lower():
            response = "Haben Sie Symptome? (Ja/Nein)"
        elif "ja" in user_message.lower():
            response = "Welche Symptome haben Sie? (Kopfschmerzen, Fieber, Husten)"
        elif any(symptom in user_message.lower() for symptom in ["kopfschmerzen", "fieber", "husten"]):
            response = "Ich empfehle Ihnen, einen Termin zu vereinbaren. Wählen Sie eine Uhrzeit: (10:00, 14:00, 16:00)"
        elif user_message in ["10:00", "14:00", "16:00"]:
            response = f"Ihr Termin um {user_message} ist bestätigt. Gute Besserung!"
        else:
            response = "Ich habe nicht verstanden. Können Sie das wiederholen?"


        return render_template('conversation.html', user_message=user_message, response=response)

    return render_template('conversation.html', response="Willkommen! Wie kann ich Ihnen helfen?")

if __name__== '_main_':
    app.run(debug=True, host ='127.0.0.1', port =5000)
    print("Verbindung geschlossen.")