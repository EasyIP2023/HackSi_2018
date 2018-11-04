class HomeController < ApplicationController
  skip_before_action :verify_authenticity_token # Disable CSRF tokens on home

  respond_to :html, :js

  def index
    if params['beacon']
      Thread.new { HomeMailer.touch_email(params['beacon']).deliver_now }
      Thread.new { Home.send_text(params['beacon']) }
      respond_to do |format|
        format.html {}
        format.js { render js: "addOurMerdianImg();" }
      end
    else
      respond_to do |format|
        format.html {}
        format.js { render js: "addMerdianImg();" }
      end
    end
  end
end
