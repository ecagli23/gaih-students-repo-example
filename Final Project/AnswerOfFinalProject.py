print("---Knowledge Competition---")
Questions = ["Türkiye Süper Liginde 4 yıldızı olan futbol takımı hangisidir?",
"İnce Memed kimin eseridir?",
"Fransız ihtilali ne zaman gerçekleşmiştir?" ,
"İstanbul kim feth etmiştir?" ,
"Göbeklitepe hangi şehirdedir?",
"Kuyucaklı Yusuf adlı eser kime aittir?",
"Bir elektrik devresinde direnç hangi harfle gösterilir?",
"Fasın başkenti hangi şehirdir?",
"Çanakkale Zaferi hangi savaşa dahildir?",
"Dünyanın en yüksek dağının adı nedir?"]
Answers = ["Galatasaray","Yaşar Kemal","1789","Fatih Sultan Mehmet","Şanlıurfa","Sabahattin Ali", "R","Rabat", "1.Dünya Savaşı","Everest"]

score = 0
for i in range(len(Questions)):
  print(Questions[i])
  x=input()
  if(x==Answers[i]):
    score +=10
if score < 20:
  print(f"you are unsuccessful , you're score is {score}")    
else:
  print(f"you are successful , you're score is {score}")