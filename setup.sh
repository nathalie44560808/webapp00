mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"2407831@escolas.anchieta.br\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
#
