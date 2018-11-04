require 'rubygems'
require 'textmagic-ruby'

$client = Textmagic::REST::Client.new ENV["TEXTMAGIC_USER"], ENV["TEXTMAGIC_TOKEN"]
