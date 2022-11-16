from fastapi import FastAPI
import scrape

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "heloo"}

@app.get("/data")
async def get_data(countries: str = 'all', fields: str = 'all'):
    data = scrape.get_cov_data()

    if countries == 'all' and fields == 'all':
        return data
    elif countries != 'all' and fields == 'all':
        return {country: data[country] for country in countries.split()}
    elif countries == 'all' and fields != 'all':
        return {country: {field: data[country][field] for field in fields.split()} for country in data.keys()}
    else:
        return {country: {field: data[country][field] for field in fields.split()} for country in countries.split()}
