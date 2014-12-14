require 'csv'

CSV.open("submission/simple.csv", "wb") do |csv|
  csv << ["Id", "Solution"]
  (1..9000).each do |i|
    csv << [i, Random.new.rand(0...1)]
  end
end
