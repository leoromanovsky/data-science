require 'csv'

CSV.open("test_sub.csv", "wb") do |csv|
  csv << ["PassengerId", "Survived"]
  (0..417).each do |i|
    csv << [892 + i, Random.new.rand(0...1)]
  end
end
