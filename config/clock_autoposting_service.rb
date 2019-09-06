while true
  puts "**************************************************************"
  puts " Publish at: #{Time.now.getlocal('-08:00')} of #{Date.now} "
  system("ruby services/autoposting/tweet_posting.rb")
  puts ".............................................................."
  sleep 28780
end