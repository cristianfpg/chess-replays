type SearchInputProps = {
    turn: number;
    onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
};

const SearchInput = ({ turn, onChange }: SearchInputProps) => {
    return <input type="number" value={turn} onChange={onChange}/>
};

export default SearchInput;