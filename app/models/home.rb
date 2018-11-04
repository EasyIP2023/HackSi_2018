class Home
  def self.send_text(users, message)
    i = 0
    numbers = []
    users.each do |u|
      numbers[i] = "+1#{u.phone}"
      i += 1
    end
    $client.messages.create(phones: "#{numbers.join(',')}", text: message) }
  end
end
