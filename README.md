# Prevent Test Writes Production Environment

This example demonstrates how to prevent test suites or any non-production code from writing data to a production environment. It uses an environment variable (`APP_ENV`) to differentiate between environments and conditionally blocks write operations when in 'production' mode. This pattern helps maintain data integrity and security.

## Language

`python`

## How to Run

Save the code as `main.py`.
Run from your terminal: `python main.py`

## Original Article

This example accompanies the Turkish article: [Test Suites'in Üretim Ortamına Yazması: Nasıl Bir Hata Bulduk ve Neler Yaptık?](https://fatihsoysal.com/blog/test-suitesin-uretim-ortamina-yazmasi-nasil-bir-hata-bulduk-ve-neler-yaptik/).

## License

MIT — see [LICENSE](LICENSE).
