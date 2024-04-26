'use client';

import Question from '@/components/Question';
import { listOfQuestions } from '@/components/listOfQuestions';
import { useState } from 'react';

export default function Home() {
	const [showAll, setShowAll] = useState(false);
	const [clearAll, setClearAll] = useState(false);
	const [list, setList] = useState(listOfQuestions);
	const [allQuestions, setAllQuestions] = useState(listOfQuestions);

	const shuffle = (unshuffled: typeof listOfQuestions) =>
		unshuffled
			.map((value) => ({ value, sort: Math.random() }))
			.sort((a, b) => a.sort - b.sort)
			.map(({ value }) => value);

	return (
		<main className='flex min-h-screen flex-col p-3 pt-10 md:p-24'>
			<div className='flex gap-2 w-full fixed top-0 right-0 justify-center'>
				<button
					className='bg-white text-black px-4 py-1 rounded-md m-2'
					onClick={() => {
						setClearAll(!clearAll);
						setList(shuffle(list));
					}}
				>
					Shuffle
				</button>
				<button
					className='bg-green-800 text-white px-4 py-1 rounded-md m-2'
					onClick={() => setShowAll(!showAll)}
				>
					Show all
				</button>
				<button
					className='bg-red-800 text-white px-4 py-1 rounded-md m-2'
					onClick={() => setClearAll(!clearAll)}
				>
					Clear all
				</button>
			</div>
			{list.map((e, i) => (
				<Question
					number={i + 1}
					question={e.question}
					options={e.options}
					answer={e.options[e.correct]}
					showAll={showAll}
					clearAll={clearAll}
					id={e.id}
					allQuestions={allQuestions}
					setAllQuestions={setAllQuestions}
				/>
			))}
		</main>
	);
}
