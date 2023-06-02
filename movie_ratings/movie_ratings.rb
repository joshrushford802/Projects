movies = {
  godzilla: 5
}

puts "Enter a movie: "
choice = gets.chomp.downcase

case choice
  when "add"
    print "Movie title - "
    title = gets.chomp.downcase

    if movies[title.to_sym] == nil
      print "Rating - "
      rating = gets.chomp
      movies[title.to_sym] = rating.to_i
    else
      puts "Movie already added."
    end

  when "update"
    print "Enter movie title - "
    title = gets.chomp.downcase

    if movies[title.to_sym] == nil
      puts "Movie not found."
    else
      print "New rating - "
      rating = gets.chomp
      movies[title.to_sym] = rating.to_i
    end

  when "display"
    movies.each { |title, rating| puts "#{title.capitalize}: #{rating}" }
  when "delete"
    print "Enter movie title - "
    title = gets.chomp.downcase
    if movies[title.to_sym] == nil
      puts "Movie not found."
    else
      movies.delete(title.to_sym)
      puts "Movie deleted."
    end
  else
    puts "Error!"
end