pipeline{
	agent any
	stages{
		stage("Build"){
			steps{
				echo "Builidng....!"
				echo "Built."
			}
		}
		stage("Test"){
			steps{
				echo "Testing....."
				echo "Tested."
			}
		}
		stage("Deploy"){
			steps{
				bat "python python.py"
			}
		}
	}
}
	
		
