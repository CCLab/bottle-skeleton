desc "Lint the Python code"
task :pylint do 
  puts "-----------------------------"
  puts ">> Linting the Python code"
  puts "-----------------------------"

  sh 'pychecker --limit 30 main.py ./app/*py'

  puts "-----------------------------"
  puts ">> Python code looks fine"
  puts "-----------------------------"
end

desc "Lint the JavaScript code"
task :jslint do 
  puts "---------------------------------"
  puts ">> Linting the JavaScript code"
  puts "---------------------------------"

  sh 'jslint --white --sub --nomen --vars --predef $ ./static/js/*js'

  puts "--------------------------------"
  puts ">> JavaScript code looks fine"
  puts "--------------------------------"
end

desc "Lints all the source code"
task :lintall => [:pylint, :jslint] do
end

desc "Run development server on localhost"
task :run => :lintall do
  sh "python main.py dev"
end

task :default => :run do
end
