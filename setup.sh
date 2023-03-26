mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"roro.silva99999@gmail.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[theme]
primaryColor = ‘#84a3a7’
backgroundColor = ‘#EFEDE8’
secondaryBackgroundColor = ‘#fafafa’
textColor= ‘#424242’
font = ‘sans serif’
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml