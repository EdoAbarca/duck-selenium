from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

start_time = time.time()

with open("logs.txt", "w", encoding="utf-8") as log:
    try:
        driver = webdriver.Chrome()
        driver.get("https://duckduckgo.com/")
        log.write("Navegador abierto y página cargada.\n")

        buscador = driver.find_element(By.NAME, "q")
        buscador.send_keys("inmuebles en Bogotá")
        buscador.send_keys(Keys.RETURN)
        log.write("Búsqueda enviada.\n")

        time.sleep(2)

        resultados = driver.find_elements(By.CSS_SELECTOR, ".react-results--main")
        assert len(resultados) > 0, "No se encontraron resultados."
        log.write(f"Resultados encontrados: {len(resultados)}\n")

        log.write("✅ Prueba funcional completada con éxito\n")
        print("✅ Prueba funcional completada con éxito")
    except Exception as e:
        log.write(f"❌ Error: {e}\n")
        print(f"❌ Error: {e}")
        raise
    finally:
        driver.quit()
        elapsed = time.time() - start_time
        log.write(f"Tiempo de ejecución: {elapsed:.2f} segundos\n")