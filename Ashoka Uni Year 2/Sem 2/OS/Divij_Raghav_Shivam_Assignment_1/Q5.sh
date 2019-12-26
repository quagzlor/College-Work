echo Enter the email
read email

if [[ "$email" =~ ^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$ ]]
then
    echo "The Email address is valid."
else
    echo "The Email address is invalid."
fi
