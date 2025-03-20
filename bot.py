import os
import datetime
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer le token du bot depuis le fichier .env
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Fonction pour la commande /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Bienvenue sur le bot de compte à rebours !\n"
        "Utilisez la commande /countdown pour voir combien de temps il reste avant la sortie."
    )

# Fonction pour la commande /countdown
def countdown(update: Update, context: CallbackContext) -> None:
    # Définir la date cible (par exemple, 2 jours plus tard)
    target_date = datetime.datetime(2025, 3, 22, 0, 0)  # Date cible (modifiez selon vos besoins)
    now = datetime.datetime.now()
    diff = target_date - now

    if diff.total_seconds() > 0:
        # Calculer les jours, heures, minutes et secondes restants
        days = diff.days
        hours = diff.seconds // 3600
        minutes = (diff.seconds % 3600) // 60
        seconds = diff.seconds % 60

        # Envoyer le message avec le compte à rebours
        update.message.reply_text(
            f"⏳ Compte à rebours :\n"
            f"{days} jours, {hours} heures, {minutes} minutes et {seconds} secondes restants !"
        )
    else:
        # Si la date cible est atteinte ou dépassée
        update.message.reply_text("🎉 Le compte à rebours est terminé !")

# Fonction principale pour démarrer le bot
def main():
    # Initialiser l'updater et le dispatcher avec le token sécurisé
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Ajouter les gestionnaires de commandes
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("countdown", countdown))

    # Démarrer le bot
    print("Le bot est en cours d'exécution...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
