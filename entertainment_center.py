import fresh_tomatoes
import media

bahubali=media.Movie("Bahubali","The empire of Mahispati Samraj","https://upload.wikimedia.org/wikipedia/en/d/dc/Baahubali_The_Beginning_Movie_Poster.jpg","https://www.youtube.com/watch?v=VdafjyFK3ko&t=5s")

son_of_satyamurthi=media.Movie("Son of Satyamurthi","The greatness of Father","https://upload.wikimedia.org/wikipedia/en/8/81/Son_of_Satyamurthy_poster.jpg","https://www.youtube.com/watch?v=bKPfqvelpNY")

nannaku_prematho=media.Movie("Nannaku Prematho","The Revenge of Son","https://upload.wikimedia.org/wikipedia/en/a/ab/Nannaku_Prematho_Telugu_Poster.jpg","https://www.youtube.com/watch?v=Om69gF1iiT4")

main_hoon_na=media.Movie("Main Hoon Na","The Brother's Love","https://upload.wikimedia.org/wikipedia/en/7/7a/Main_Hoon_Na_poster.jpg","https://www.youtube.com/watch?v=7fRLWoyLFBk")

yeh_jawani_h_deewani=media.Movie("Yeh Jawani H Deewani","Not express in just a Line","https://upload.wikimedia.org/wikipedia/en/1/15/Yeh_jawani_hai_deewani.jpg","https://www.youtube.com/watch?v=Rbp2XUSeUNE")

spyder=media.Movie("Spyder","The Mahesh Babu","https://upload.wikimedia.org/wikipedia/en/d/de/Spyder_film_poster.jpg","https://www.youtube.com/watch?v=VUEH5KTk2-E")

movies=[bahubali,son_of_satyamurthi,nannaku_prematho,main_hoon_na,yeh_jawani_h_deewani,spyder]
fresh_tomatoes.open_movies_page(movies)
