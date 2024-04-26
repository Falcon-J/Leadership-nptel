'use client';

import { Dispatch, SetStateAction, useEffect, useState } from 'react';
import { listOfQuestions } from '@/components/listOfQuestions';

export default function Question(props: {
	number: number;
	question: string;
	options: string[];
	answer: string;
	showAll: boolean;
	clearAll: boolean;
	id: number;
	allQuestions: typeof listOfQuestions;
	setAllQuestions: Dispatch<SetStateAction<typeof listOfQuestions>>;
}) {
	const [selected, setSelected] = useState(-1);

	useEffect(() => {
		setSelected(props.options.indexOf(props.answer));
	}, [props.showAll]);

	useEffect(() => {
		setSelected(-1);
	}, [props.clearAll]);

	const [options, setOptions] = useState<String[]>([]);
	useEffect(() => {
		setOptions(
			props.options
			// .map((value) => ({ value, sort: Math.random() }))
			// .sort((a, b) => a.sort - b.sort)
			// .map(({ value }) => value)
		);
	}, [props.question]);

	useEffect(() => {
		console.log(props.allQuestions);
	}, [props.allQuestions]);

	return (
		<div className='flex flex-col my-5'>
			<div className='text-lg sm:text-2xl font-bold'>
				{props.number}. {props.question}
			</div>
			<div className='flex flex-col'>
				{options.map((e, i) => (
					<div
						className='flex flex-row cursor-pointer sm:my-1 px-2 py-1'
						style={{
							backgroundColor:
								selected === i
									? e === props.answer
										? 'green'
										: 'red'
									: 'black',
						}}
						onClick={() => {
							setSelected(i);
							props.setAllQuestions((values) =>
								values.map((e) =>
									e.id === props.id
										? {
												...e,
												correct: i,
										  }
										: e
								)
							);
						}}
					>
						<div className='text-base sm:text-xl'>
							{String.fromCharCode(65 + i)}. {e}
						</div>
					</div>
				))}
			</div>
		</div>
	);
}
