import Fetch from './Fetch';

export default class Translate {
    private fetch: Fetch;

    constructor(fetch: Fetch) {
        this.fetch = fetch;
    }

    async translate(text: string): Promise<string> {
        let data = new FormData();
        data.set('text2translate', text);

        return this.fetch.post('http://ec2-35-180-242-107.eu-west-3.compute.amazonaws.com:8080', data).then(response => response.data);
    }
}