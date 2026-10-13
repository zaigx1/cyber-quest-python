python cyber_quest.pyimport random
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\\nTekan Enter untuk lanjut...")

def ask_choice(prompt, choices):
    while True:
        answer = input(prompt).strip().upper()
        if answer in choices:
            return answer
        print("Pilihan tidak valid. Coba lagi.")

def play_game():
    clear_screen()
    print("=" * 46)
    print("             CYBER QUEST")
    print("      Mini game petualangan Python")
    print("=" * 46)

    name = input("\\nNama pemain: ").strip() or "Player"
    score = 0
    hp = 3

    print(f"\\nHalo, {name}! Selesaikan 3 tantangan untuk lulus.")
    pause()

    # Tantangan 1: Tebak kode
    clear_screen()
    print("[1/3] ACCESS CODE")
    print("Tebak angka rahasia dari 1 sampai 10. Ada 3 percobaan.")
    secret = random.randint(1, 10)
    solved = False

    for attempt in range(1, 4):
        try:
            guess = int(input(f"Percobaan {attempt}/3: "))
        except ValueError:
            print("Masukkan angka, bukan teks.")
            continue

        if guess == secret:
            print("Benar! Akses terbuka. +10 poin")
            score += 10
            solved = True
            break
        elif guess < secret:
            print("Terlalu kecil.")
        else:
            print("Terlalu besar.")

    if not solved:
        print(f"Kode rahasianya: {secret}")
        hp -= 1
    pause()

    # Tantangan 2: Kuis keamanan
    clear_screen()
    print("[2/3] SECURITY QUIZ")
    print("Apa fungsi utama autentikasi dua faktor (2FA)?")
    print("A. Membagikan password ke teman")
    print("B. Menambahkan lapisan verifikasi saat login")
    print("C. Menghapus semua file")
    answer = ask_choice("Jawaban (A/B/C): ", {"A", "B", "C"})

    if answer == "B":
        print("Benar! +10 poin")
        score += 10
    else:
        print("Belum tepat. Jawaban yang benar: B")
        hp -= 1
    pause()

    # Tantangan 3: Deteksi phishing
    clear_screen()
    print("[3/3] PHISHING ALERT")
    print("Email asing meminta password lewat tautan yang mencurigakan.")
    print("Apa tindakan paling aman?")
    print("A. Klik tautan dan masukkan password")
    print("B. Abaikan verifikasi dan teruskan email")
    print("C. Jangan klik; periksa melalui kanal resmi")
    answer = ask_choice("Jawaban (A/B/C): ", {"A", "B", "C"})

    if answer == "C":
        print("Tepat! +10 poin")
        score += 10
    else:
        print("Belum tepat. Jawaban yang benar: C")
        hp -= 1
    pause()

    clear_screen()
    print("=" * 46)
    print("                 HASIL AKHIR")
    print("=" * 46)
    print(f"Pemain : {name}")
    print(f"Skor   : {score}/30")
    print(f"HP     : {max(hp, 0)}/3")

    if score == 30:
        print("RANK: CYBER GUARDIAN - Sempurna!")
    elif score >= 20:
        print("RANK: SECURITY TRAINEE - Kerja bagus!")
    else:
        print("RANK: ROOKIE - Terus belajar dan coba lagi!")

    print("\\nTerima kasih sudah bermain!")
    again = input("Main lagi? (y/n): ").strip().lower()
    if again == "y":
        play_game()
    else:
        print("Sampai jumpa!")

if __name__ == "__main__":
    play_game()
