class HomeMailer < ApplicationMailer
  default to: -> { User.active.pluck(:email) }, from: 'beaconhacksi@gmail.com'

  def touch_email(message)
    @message = message
    mail(subject: 'A NEW HAND TOUCHES THE BEACON!!!')
  end

end
