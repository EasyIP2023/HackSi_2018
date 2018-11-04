class Home
  def self.send_text(message)
    users_phone = User.active.pluck(:phone)
    users_phone.each_with_index { |up,i| users_phone[i] = "+1#{up}"}
    $client.messages.create(phones: "#{users_phone.join(',')}", text: message)
  end
end
