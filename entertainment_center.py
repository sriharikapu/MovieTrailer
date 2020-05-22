import media
import fresh_tomatoes

# Creating the instance of the Movie class
the_Avengers = media.Movie(
            "The Avengers",
            "Nick Fury is compelled to launch the Avengers Initiative"
			"when Loki poses a threat to planet Earth."
			"His squad of superheroes put their minds together"
			"to accomplish the task. "
			"- Directed by Joss Whedon (imdb.com)",
            "Action/Sci-fi", "Scarlett Johansson", "Joss Whedon", "2012",
            "https://i.pinimg.com/originals/92/c8/e0/92c8e00b34fcfdeaf605a0647c21adb3.jpg",  # noqa
            "https://www.youtube.com/watch?v=eOrNdBpGMv8")  # noqa

Bahubali_the_beginning = media.Movie(
            "Baahubali: The Beginning",
            "In the kingdom of Mahishmati, Shivudu falls in love" 
			"with a fair maiden. While trying to woo her," 
			"he learns about the conflict-ridden past of"
			"his family and his true legacy. "
            "- Directed by SS Rajamouli (imdb.com)",
            "Action", "Prabhas", "Rajamouli", "2015",
            "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQnIM8CU0VO9BpthgIHGJM_mG6xDcC5uOpY-FIuILs0r4wJcc6F",  # noqa
            "https://www.youtube.com/watch?v=VdafjyFK3ko")  # noqa

super_30 = media.Movie(
            "Super 30",
            "Anand Kumar, a mathematician from Patna, India, "
			"works his way through challenges towards success "
			"before running the Super 30 programme for IIT aspirants in Patna. "
            "- Directed by Vikas Bahl(imbd.com)",
            "Drama", "Hrithik Roshan", " Vikas Bahl", "2019",
            "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQsna1_Y2wNQ51A3HsnzxRqQYDSrWn3_kgVXd7N2mUmH1a05fhI",  # noqa
            "https://www.youtube.com/watch?v=QpvEWVVnICE")  # noqa

the_gods_must_be_crazy = media.Movie(
            "The Gods Must Be Crazy",
            "A Coca-Cola bottle dropped from an airplane raises havoc "
			"among a normally peaceful tribe of African bushmen" 
			"who believe it to be a utensil of the gods. "
			"- Directed by Jamie Uys(imbd.com)",
            "Comedy/Slapstick ", "Nǃxau ǂToma", " Jamie Uys", "1980",
            "https://www.gstatic.com/tv/thumb/v22vodart/8763/p8763_v_v8_aa.jpg",  # noqa
            "https://www.youtube.com/watch?v=3EG0dH1oN7k")  # noqa
			
raju_gari_gadhi_3 = media.Movie(
            "Raju Gari Gadhi 3",
            "Ashwin and Maya, a couple in love, learn of the presence of "
			"an evil spirit in their life. Determined to bring their life"
			"back to normalcy, Ashwin sets out on a spooky journey to " 
			"safeguard his love."
			"- Directed by Omkar(imbd.com)",
            "Horror/Triller ", "Avika Gor", " Omkar", "2019",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTlCQCl_942L25O7csT28VwYX2ysjKC3qyw3iawNa3SLaTCWfM",  # noqa
            "https://www.youtube.com/watch?v=boJtBqIJ6Ls&feature=emb_title")  # noqa
			



# Creating a list containing the instances of the Movie just created
movies = [the_Avengers, Bahubali_the_beginning, super_30, the_gods_must_be_crazy, raju_gari_gadhi_3]

# Calling the open_movies_page to create the page with the Movies
fresh_tomatoes.open_movies_page(movies, media.Movie.TOTAL_INSTANCES)
